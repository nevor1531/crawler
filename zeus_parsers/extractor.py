# coding: utf-8
__author__ = 'nevor'
from procedure import parse_procedures


class Extractor():
    def __init__(self):
        self.name = None
        self.urls_procedures = None
        self.extractors = None
        self.entity = None
        self.condition_procedures = None
        self.meta_procedures = None
        self.last = False


class ExtratorParser():

    def __init__(self):
        self.all_extractors = dict()

    def parse_extractors(self, conf, entity_map):
        if type(conf) != list:
            conf = [conf]

        extractors = list()
        for c in conf:
            extractors.append(self.parse_extractor(c, entity_map))

        return extractors

    def parse_extractor(self, conf, entity_map):
        if isinstance(conf, basestring):
            if conf not in self.all_extractors:
                raise Exception('unkonw extractor %s' % conf['extends'])
            return self.all_extractors[conf]

        extractor = Extractor()
        extractor.name = conf.get('name', None)

        # put extractor in map
        if extractor.name:
            if extractor.name in self.all_extractors:
                raise Exception('duplicatd extractor name "%s"' % extractor.name)
            self.all_extractors[extractor.name] = extractor

        if 'extends' in conf:
            if conf['extends'] not in self.all_extractors:
                raise Exception('unkonw extractor %s' % conf['extends'])

            base_extractor = self.all_extractors[conf['extends']]
            extractor.urls = base_extractor.urls
            extractor.parsers = base_extractor.parsers
            extractor.entity = base_extractor.entity
            extractor.condition_procedures = base_extractor.condition_procedures
            extractor.last = base_extractor.last

        if 'condition' in conf:
            extractor.condition_procedures = parse_procedures(conf['condition'])

        if 'urls' in conf:
            extractor.urls_procedures = parse_procedures(conf['urls'])

        if 'entity' in conf:
            if conf['entity'] not in entity_map:
                raise Exception('unkonw entity "%s"' % conf['entity'])

            extractor.entity = entity_map[conf['entity']]

        if 'extractors' in conf:
            extractor.extractors = self.parse_extractors(conf['extractors'], entity_map)

        if 'meta' in conf:
            extractor.meta_procedures = dict()
            for key, value in conf['meta'].items():
                extractor.meta_procedures[key] = parse_procedures(value)

        if 'last' in conf:
            extractor.last = conf['last']

        return extractor

if __name__ == '__main__':
    pass
