from main import test
import yacc as Yacc
from lexer import tokens
from intermediate import array,binary_search_tree,doubly_linked_list,queue,stack
import logging
#source ./venv/Scripts/activate
#run this in terminal to activate venv

### Declarations and stuff ###
parser= Yacc.yacc()
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
def parser_Function(x):
    ''' 
        Function : DEF CANVAS Canvas DEF STRUCTURES Structure DEF DRAW Draw 
    '''
    ###Read the next existing definition of token for assured correct input
    dictionary[x[2]] = x[3]
    dictionary[x[5]] = x[6]
    dictionary[x[8]] = x[9]


def parser_Boolean(x):
    '''
        Bool : true | false
    '''
    #default true
    x[0]=x[1]

def parser_Canvas(x):
    '''
         Canvas : LP Dimensions Position RP
    '''
    #adopting to the dimension and position
    x[0] = [x[2], x[3]]

def parser_Dimensions(x):
    '''
         Dimensions : DIMENSIONS COLON LESSTHAN INTEGER COMMA INTEGER GREATERTHAN
    '''
    #adopting to the tuple
    x[0] = (x[4], x[6])

def parser_Color(x):
    '''
        Color: BLACK | BLUE
    '''
    #default black
    x[0]=x[1]

def parser_Structure(x):
    '''
        Structure : LP Struct RP              
    '''
    x[0]= x[2]

def parser_Struct(x):
    '''
        Struct: STRUCT Colon DataStructure
    '''
    x[0]= x[3]

def parser_DataStructure(x):
    '''
        DS : ARRAY | QUEUE | STACK | DLL | BST
    '''
    #default array
    x[0]=x[1]

def parser_Array(x):
    '''
        Arr : Array
    '''
    x[0]=x[1]


def parser_int(x):
    '''
        Int : Digit | Digit Integer
    '''
    x[0]=x[1]

def parser_error(x):
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

elif structure == "doublyLinkedList":
    dllVal=structureValue[1]
    dll=doubly_linked_list.DoublyLinkedList(dllVal, dimensions, position)
    dll.draw()

else:
    print("Structure not yet developed.")

