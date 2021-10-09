import time
import turtle
import drawing_builder as db

class Stack:
    def __init__(self):
        self.items = []
        self.height = 50

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __draw_stack(self, pencil_color, filling_color):
        drawing = turtle.Turtle()
        drawing.color(pencil_color, filling_color)
        drawing.speed(10)
        for pos, item in enumerate(self.items):

            db.square(drawing, self.height)
            # draw value in the middle of the square
            db.write_text(drawing, item, self.height/2)

            # moves the pen to the next starting position
            if pos + 1 != self.size():
                drawing.forward(self.height)
                drawing.right(90)
        return drawing

    def draw_peek(self, pencil_color='black', filling_color='red'):
        drawing = self.__draw_stack(pencil_color, filling_color)
        drawing.penup()
        drawing.right(180)
        drawing.forward(self.height / 2)
        drawing.pendown()
        drawing.circle(self.height/2)
        time.sleep(5)

    def draw(self, pencil_color='black', filling_color='red'):
        self.__draw_stack(pencil_color, filling_color)
        time.sleep(5)


test = Stack()
for _ in range(3):
    test.push(_)
test.draw_peek()
