import time
import turtle


def square(drawing: turtle.Turtle, height: int, rotation='right'):
    if rotation == 'right':
        drawing.forward(height)
        drawing.right(90)
        drawing.forward(height)
        drawing.right(90)
        drawing.forward(height)
        drawing.right(90)
        drawing.forward(height)
    else:
        drawing.forward(height)
        drawing.left(90)
        drawing.forward(height)
        drawing.left(90)
        drawing.forward(height)
        drawing.left(90)
        drawing.forward(height)


def write_text(drawing: turtle.Turtle, data, height: float, rotation='right', align='center'):
    if rotation == 'right':
        drawing.penup()
        drawing.right(90)
        drawing.forward(height)
        drawing.right(90)
        drawing.forward(height)
        drawing.write(data, False, align=align)
        drawing.right(90)
        drawing.forward(height)
        drawing.right(90)
        drawing.forward(height)
        drawing.pendown()
    else:
        drawing.penup()
        drawing.left(90)
        drawing.forward(height)
        drawing.left(90)
        drawing.forward(height)
        drawing.write(data, False, align=align)
        drawing.left(90)
        drawing.forward(height)
        drawing.left(90)
        drawing.forward(height)
        drawing.pendown()