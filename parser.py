from main import test
import yacc as Yacc
from lexer import tokens
from intermediate import array,binary_search_tree,doubly_linked_list,queue,stack
import logging
#source ./venv/Scripts/activate
#run this in terminal to activate venv

### Declarations and stuff ###
parser = Yacc.yacc()
log = logging.getLogger()
dictionary = dict() 


logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)

while True:
    try:
        s = test('test')
    except EOFError:
        break
    parser.parse(s, debug=log)
    break


###     DEFINITIONS      ###
def p_Func(p):
    ''' 
        Function : DEF CANVAS Canvas DEF STRUCTURES Structure DEF DRAW Draw 
    '''
    ###Read the next existing definition of token for assured correct input
    dictionary[p[2]] = p[3]
    dictionary[p[5]] = p[6]
    dictionary[p[8]] = p[9]


def p_Boolean(p):
    '''
        Bool : true | false
    '''
    #default true
    p[0]=p[1]

def p_Canvas(p):
    '''
         Canvas : LP Dimensions Position RP
    '''
    #adopting to the dimension and position
    p[0] = [p[2], p[3]]

def p_Dimensions(p):
    '''
         Dimensions : DIMENSIONS COLON LESSTHAN INTEGER COMMA INTEGER GREATERTHAN
    '''
    #adopting to the tuple
    p[0] = (p[4], p[6])

def p_Color(p):
    '''
        Color : BLACK | BLUE
    '''
    #default black
    p[0]=p[1]

def p_Structure(p):
    '''
        Structure : LP Struct RP              
    '''
    p[0]= p[2]

def p_Struct(p):
    '''
        Struct : STRUCT Colon DataStructure
    '''
    p[0]= p[3]

def p_DataStructure(p):
    '''
        DS : ARRAY | QUEUE | STACK | DLL | BST
    '''
    #default array
    p[0]=p[1]

def p_Array(p):
    '''
        Arr : Array
    '''
    p[0]=p[1]


def p_int(p):
    '''
        Int : Digit | Digit Integer
    '''
    p[0]=p[1]

def p_error(p):
    print("Registered syntax error.")



###     Intermediate Code Connection        ###

if len(dictionary['draw']) == 3:
    dimensions = dictionary['canvas'][0]   # dimensions of the screen
    position = dictionary['canvas'][2]         # tuple (x,y) x=pixels from left fo screen, y=pixels from top of screen
    structure=dictionary['structures'][0]      # type of data structures
    structureValue=dictionary['structures'][1] # data (list)

else:
    dimensions = dictionary['canvas'][0]
    position = dictionary['canvas'][2]
    structure= dictionary['draw'][4][0]
    structureValue=dictionary['draw'][4][1]


if structure=='array':
#     arrayVal=structureValue[1]
#     array=array.arrayclassnameholder(arrayVal, dimensions, position)
#     array.draw()
    print("yes")
    
elif structure=='queue':
    queueVal=structureValue[1]
    queue=queue.Queue(queueVal, dimensions, position)
    queue.draw()
    
elif structure=="stack":
    stackVal=structureValue[1]
    stack=stack.Stack(stackVal, dimensions, position)
    stack.draw()

# elif structure == "doublyLinkedList":
#     dllVal=structureValue[1]
#     dll=doubly_linked_list.DoublyLinkedList(dllVal, dimensions, position)
#     dll.draw()

else:
    print("Structure not yet developed.")

