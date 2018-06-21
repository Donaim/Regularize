

import re
from functools import reduce

re_tok = re.compile(r'[ ,=:\(\)]+')
re_line = re.compile(r'\n+')
re_ignore = re.compile(r'(^\s*def\s.*)|(^\s*$)')

def count_tokens(text : str) -> int:
    return len(list(get_tokens(text)))

def get_tokens(text : str) -> iter:
    lines = split_by_lines(text)
    lines = filter(lambda x: not ignore_line_q(x), lines)
    tokens = map(lambda x: split_by_tokens(x), lines)
    tokens = reduce(lambda a, b: a + b, tokens, [])
    return tokens

def split_by_tokens(line : str):
    return list(filter(lambda x: len(x) > 0, re_tok.split(line)))
def split_by_lines(text : str):
    return re_line.split(text)

def ignore_line_q(line : str):
    return bool(re_ignore.match(line))

