import time
import turtle
import drawing_builder as db


class Queue:
    def __init__(self):
        self.items = []
        self.height = 50

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def draw(self):
        drawing = turtle.Turtle()
        drawing.speed(10)
        for pos, item in enumerate(self.items):

            db.square(drawing, self.height, rotation='left')
            # draw value in the middle of the square
            db.write_text(drawing, item, self.height / 2, rotation='left')

            # moves the pen to the next starting position
            if pos + 1 != self.size():
                drawing.forward(self.height)
                drawing.left(90)
        time.sleep(10)


test = Queue()
for i in range(10):
    test.enqueue(i)
test.draw()