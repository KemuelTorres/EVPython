import time
import turtle
from . import drawing_builder as db

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

    def draw(self):
        x = -100
        y = self.height * 3
        speed = 10
        drawing = db.set_up(speed, x, y, "Array", "A collection of items stored at contiguous memory locations.")
        index = 0
        for pos, item in enumerate(self.items):
            db.square(drawing, self.height, rotation='left')
            # draw value in the middle of the square
            db.write_text(drawing, item, round(self.height / 2), rotation='left')

            db.write_text_offset(drawing, index, round(self.height / 2), rotation='left')
            index += 1
            # Playing around with drawing, must fix!
            if pos + 1 != self.size():
                drawing.forward(0)
                drawing.left(90)
        time.sleep(10)

