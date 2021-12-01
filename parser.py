from main import test
import ply.yacc as yacc
from lexer import tokens
from intermediate import binary_search_tree, doubly_linked_list, queue, stack
import logging
#source ./venv/Scripts/activate
#run this in terminal to activate venv

### Declarations and stuff ###
dictionary = dict() 


logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)


###     DEFINITIONS      ###
def p_Func(p):
    '''
        Func : DEF CANVAS Canvas DEF STRUCTURES Structure
    '''
    dictionary[p[2]] = p[3]
    dictionary[p[5]] = p[6]

def p_Bool(p):
    '''
        Bool : true
             | false
    '''
    #default true
    p[0] = p[1]

def p_Canvas(p):
    '''
        Canvas : left_parenthesis Dimensions Position right_parenthesis
    '''
    #adopting to the dimension and position
    p[0] = [p[2], p[3]]

def p_Position(p):
    '''
        Position : POSITION colon less_than integer comma integer greater_than
    '''
    p[0] = (p[4], p[6])

def p_Dimensions(p):
    '''
        Dimensions : DIMENSIONS colon less_than integer comma integer greater_than
    '''
    #adopting to the tuple
    p[0] = (p[4], p[6])

def p_Color(p):
    '''
        Color : BLACK
              | BLUE
    '''
    #default black
    p[0]=p[1]

def p_Structure(p):
    '''
        Structure : left_parenthesis Struct right_parenthesis              
    '''
    p[0]= p[2]

def p_Struct(p):
    '''
        Struct : STRUCT colon DataStructure
    '''
    p[0]= p[3]

def p_DataStructure(p):
    '''
        DataStructure : ARRAY
                      | QUEUE
                      | STACK
                      | DLL
                      | BST
    '''
    #default array
    p[0]=p[1]

def p_int(p):
    '''
    Int : digit 
        | digit integer
    '''
    p[0]=p[1]

def p_error(p):
    print("Registered syntax error.")

parser = yacc.yacc()
log = logging.getLogger()

while True:
    try:
        s = test('test')
    except EOFError:
        break
    parser.parse(s, debug=log)
    break


###     Intermediate Code Connection        ###
### Declarations and stuff ###
print(dictionary)


canvasDimension = dictionary['canvas'][0]
structPosition = dictionary['canvas'][1]
structure = dictionary['structures']

match structure:
    case "queue":
        testa = queue.Queue()
        for i in range(10):
            testa.enqueue(i)
        testa.draw()
    case "doublyLinkedList":
        testa = doubly_linked_list.DoublyLinkedList()
        
        for i in range(5):
            testa.add(i)
        testa.draw()
    case "stack":
        testa = stack.Stack()
        for _ in range(6):
            testa.push(_)
        testa.draw_peek()
    case "binary_search_tree":
        binary_search_tree.BinarySearchTree()
    case _:
        print(f"The Structure {structure} you desire is not available")