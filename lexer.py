import lex

tokens = [
    'DIGIT',
    'LP',
    'RP',
    'LB',
    'RB',
    'COMMA',
    'COLON',
    'LESSTHAN',
    'GREATERTHAN',
    'ARRAY',
    'INTEGER'
]
keywords = {
    'true': 'true',
    'false': 'false',
    'def': 'DEF',
    'canvas': 'CANVAS',
    'structures': 'STRUCTURES',
    'draw': 'DRAW',
    'dimensions': 'DIMENSIONS',
    'position': 'POSITION',
    # '': '',
}
colors = {
    'black': 'black',
    'blue': 'blue'
}
structures = {
    'array': 'ARRAY',
    'queue': 'QUEUE',
    'stack': 'STACK',
    'doublyLinkedList': 'DLL',
    'binarySearchTree': 'BST',
}
tokens += list(keywords.values()) + list(colors.values()) + list(structures.values())

left_parenthesis = r'\('
right_parenthesis = r'\)'
left_bracket = r'\['
right_bracket = r'\]'
colon = r'\:'
comma = r'\,'
less_than = r'\<'
greater_than = r'\>'
digit = r'[0-9]'


def reserved_word_token(token):
    # reserved_words = ' | '.join(keywords.values())
    if token.value in keywords:
        token.type = keywords[token.value]
    return token


def reserved_colors_token(token):
    # reserved_words = ' | '.join(keywords.values())
    if token.value in colors:
        token.type = keywords[token.value]
    return token


def reserved_structure_token(token):
    # reserved_words = ' | '.join(keywords.values())
    if token.value in structures:
        token.type = keywords[token.value]
    return token


def integer_token(token):
    token.value = int(token.value)
    return token


def t_new_line(token):
    token.lexer.lineno += len(token.value)


def t_error(token):
    print("invalid chapters")
    token.lexer.skip(1)


# lexer = lex.lex()
# lexer.input("banana")
#
# while True:
#     tok = lexer.token()
#     if not tok:
#         break