
import re

TOKEN_SPEC = [
    ('NUMBER',   r'\d+(\.\d*)?'),
    ('IDENT',    r'[a-zA-Z_]\w*'),
    ('OP',       r'[\+\-\*/\^=]'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('COMMA',    r','),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.'),
]

TOKEN_REGEX = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)

def tokenize(code):
    for mo in re.finditer(TOKEN_REGEX, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected token: {value}')
        yield (kind, value)
