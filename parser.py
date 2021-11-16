import yacc as Yacc
from lexer import tokens
from intermediate import array,binary_search_tree,doubly_linked_list,queue,stack

#source ./venv/Scripts/activate
#run this in terminal to activate venv

parser= Yacc.yacc()

# Below is the parser

dictionary = dict() 

def parser_Function(p):
    ''' 
        Function : DEF CANVAS Canvas DEF STRUCTURES Structure DEF DRAW Draw 
    '''
def parser_Boolean(p):
    '''
        Bool : true | false
    '''

def parser_Canvas(p):
    '''
         Canvas : LP Dimensions Position RP
    '''

def parser_Dimensions(p):
    '''
         Dimensions : DIMENSIONS COLON LESSTHAN INTEGER COMMA INTEGER GREATERTHAN
    '''

def parser_Color(p):
    '''
        Color: BLACK | BLUE
    '''

def parser_Structure(p):
    '''
        Structure : LP Struct Data RP              
    '''

