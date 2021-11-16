import time
import drawing_builder as db
import turtle

class Array:

    # Initializing Array
    def __init__(self):
        self.items = []
        self.height = 50

    # Check if Array is empty
    def is_empty(self):
        return self.items == []

    # Insert item into Array
    def insert(self, item):
        self.items.append(item)

    # Insert item into Array in a specified index
    def index_insert(self, index, item):
        if index.isNumeric():
            self.items.insert(index, item)
        else:
            raise ValueError("Provided value for index is not numerical.")

    # Remove item from Array
    def remove(self, item):
        if item in self.items:
            return self.items.remove(item)

    # Remove item at specified index from Array
    def index_remove(self, index):
        if index.isNumeric():
            self.items.pop(index)
        else:
            raise ValueError("Provided value for index is not numerical.")

    # Returns size of Array
    def size(self):
        return len(self.items)

    # width, height = 600, 600
    # screen = turtle.Screen()
    # screen.setup(width + 4, height + 8)
    # screen.setworldcoordinates(0, 0, width, height)
    # screen.title("EVPython GUI")
    # screen.bgcolor("white")
    # turtle.done()

    def draw(self):
        x = -400
        y = self.height * 3
        speed = 1
        drawing = db.set_up(speed, x, y, "Array", "A collection of items stored at contiguous memory locations.")

        for pos, item in enumerate(self.items):
            db.square(drawing, self.height, rotation='right')
            # draw value in the middle of the square
            db.write_text(drawing, item, round(self.height / 2), rotation='right')

            # Playing around with drawing, must fix!
            if pos + 1 != self.size():
                drawing.forward(self.height)
                drawing.left(90)
                turtle.penup()
                drawing.forward(self.height)
                drawing.left(90)
                turtle.pendown()
                drawing.forward(self.height)
                drawing.left(90)
                turtle.penup()
        time.sleep(10)


test = Array()
for i in range(10):
    test.insert(i)
test.draw()
