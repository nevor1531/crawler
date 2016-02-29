# coding: utf-8
__author__ = 'nevor'
import re
import json

def load(fp, *args, **kwargs):
    lines = fp.readlines()
    lines = map(iscomment, lines)
    return json.loads(''.join(lines), *args, **kwargs)

def loads(s, *args, **kwargs):
    lines = s.split("\n")
    lines = map(iscomment, lines)
    return json.loads(''.join(lines), *args, **kwargs)


def iscomment(line):
    if re.match('^\s*//.*$', line):
        return '\n'
    else:
        return line


if __name__ == '__main__':
    j = loads(open('../zeus_templates/www.lady8844.com.json').read())
    print j
