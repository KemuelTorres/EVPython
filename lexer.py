from ply import lex as lex
from main import test


tokens = [
    'digit',
    'left_parenthesis',
    'right_parenthesis',
    'left_bracket',
    'right_bracket',
    'comma',
    'colon',
    'less_than',
    'greater_than',
    'integer'
]
keywords = {
    'true': 'true',
    'false': 'false',
    'def': 'DEF',
    'canvas': 'CANVAS',
    'structures': 'STRUCTURES',
    'struct': 'STRUCT',
    # 'draw': 'DRAW',
    'dimensions': 'DIMENSIONS',
    'position': 'POSITION',
    # '': '',
}
colors = {
    'BLACK' : 'BLACK',
    'BLUE' : 'BLUE'
}
structures = {
    'array': 'ARRAY',
    'queue': 'QUEUE',
    'stack': 'STACK',
    'doublyLinkedList': 'DLL',
    'binarySearchTree': 'BST',
}
tokens += list(keywords.values()) + list(colors.values()) + list(structures.values())

t_left_parenthesis = r'\('
t_right_parenthesis = r'\)'
t_left_bracket = r'\['
t_right_bracket = r'\]'
t_colon = r'\:'
t_comma = r'\,'
t_less_than = r'\<'
t_greater_than = r'\>'
t_digit = r'[0-9]'

t_ignore = ' \t'


def t_KEYWORDS(token):
    r'def | canvas | structures | dimensions | position | struct'
    if token.value in keywords:
        token.type = keywords[token.value]
    return token


def t_COLORS(token):
    r'BLACK | BLUE'
    if token.value in colors:
        token.type = colors[token.value]
    return token


def t_STRUCTURES(token):
    r'array | queue | stack | doublyLinkedList | binarySearchTree'
    if token.value in structures:
        token.type = structures[token.value]
    return token


def t_integer(token):
    r'\d+'
    token.value = int(token.value)
    return token


def t_newLine(token):
    r'\n+'
    token.lexer.lineno += len(token.value)


def t_error(token):
    print("invalid syntax")
    token.lexer.skip(1)


lexer = lex.lex()
lexer.input(test("test"))

while True:
    tok = lexer.token()
    if not tok:
        break