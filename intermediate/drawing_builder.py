import time
import turtle


def draw_node(drawing: turtle.Turtle, width: int, data):
    x = drawing.xcor()
    y = drawing.ycor()
    drawing.forward(width)
    drawing.right(90)
    drawing.forward(width)
    drawing.right(90)
    drawing.forward(width)
    drawing.right(90)
    drawing.forward(width)
    # find center
    drawing.penup()
    drawing.goto(drawing.xcor() + width / 2, drawing.ycor() - width / 2)
    drawing.write(data, align="center")
    # move to bottom left
    drawing.goto(drawing.xcor() - width / 2, drawing.ycor() - width / 2)
    drawing.right(180)
    # draw bottom boxes
    drawing.pendown()
    drawing.forward(width / 2)
    drawing.right(270)
    drawing.forward(width)
    drawing.right(270)
    drawing.forward(width / 2)
    # move to center from top left
    drawing.penup()
    drawing.goto(drawing.xcor() - (width / 2), drawing.ycor() - width / 4)
    drawing.write("next", align="center")
    # move to middle left
    drawing.goto(drawing.xcor() + (width / 2), drawing.ycor())
    drawing.pendown()
    drawing.left(270)
    # draws arrow
    arrow(drawing, round(width / 2), direction='right')
    drawing.penup()
    # move to bottom left
    drawing.goto(drawing.xcor()-width, drawing.ycor() - width / 4)
    drawing.right(90)
    # draw bottom boxes
    drawing.pendown()
    drawing.forward(width / 2)
    drawing.right(270)
    drawing.forward(width)
    drawing.right(270)
    drawing.forward(width / 2)
    # move to center from top left
    drawing.penup()
    drawing.goto(drawing.xcor() - width / 2, drawing.ycor() - width / 4)
    drawing.write("prev", align="center")
    # move to middle right
    drawing.goto(drawing.xcor() - (width / 2), drawing.ycor())
    drawing.pendown()
    drawing.left(90)
    # draws arrow
    arrow(drawing, round(width / 2))
    #move back to starting point
    drawing.penup()
    drawing.goto(x, y)
    drawing.right(180)
    return x + width + round(width/2)

def draw_last_node(drawing: turtle.Turtle, width: int, data):
    x = drawing.xcor()
    y = drawing.ycor()
    drawing.forward(width)
    drawing.right(90)
    drawing.forward(width)
    drawing.right(90)
    drawing.forward(width)
    drawing.right(90)
    drawing.forward(width)
    # find center
    drawing.penup()
    drawing.goto(drawing.xcor() + width / 2, drawing.ycor() - width / 2)
    drawing.write(data, align="center")
    # move to bottom left
    drawing.goto(drawing.xcor() - width / 2, drawing.ycor() - width / 2)
    drawing.right(180)
    # draw bottom boxes
    drawing.pendown()
    drawing.forward(width / 2)
    drawing.right(270)
    drawing.forward(width)
    drawing.right(270)
    drawing.forward(width / 2)
    # move to center from top left
    drawing.penup()
    drawing.goto(drawing.xcor() - (width / 2), drawing.ycor() - width / 4)
    drawing.write("next", align="center")
    # move to middle left
    drawing.goto(drawing.xcor() + (width / 2), drawing.ycor())
    drawing.pendown()
    drawing.left(270)
    drawing.penup()
    # move to bottom left
    drawing.goto(drawing.xcor()-width, drawing.ycor() - width / 4)
    drawing.right(90)
    # draw bottom boxes
    drawing.pendown()
    drawing.forward(width / 2)
    drawing.right(270)
    drawing.forward(width)
    drawing.right(270)
    drawing.forward(width / 2)
    # move to center from top left
    drawing.penup()
    drawing.goto(drawing.xcor() - width / 2, drawing.ycor() - width / 4)
    drawing.write("prev", align="center")
    # move to middle right
    drawing.goto(drawing.xcor() - (width / 2), drawing.ycor())
    drawing.pendown()
    drawing.left(90)
    # draws arrow
    arrow(drawing, round(width / 2))
    #move back to starting point
    drawing.penup()
    drawing.goto(x, y)
    drawing.right(180)
    return x + width + round(width/2)


def set_up(speed: int, x_cord: float, y_cord: float, structure: str, description: str, place_below=False):
    drawing = turtle.Turtle()
    drawing.speed(speed)
    drawing.penup()
    if place_below:
        drawing.goto(x_cord, y_cord - 150)
        drawing.write(structure, font=("Arial", 25, "bold"))
        drawing.goto(x_cord, y_cord - 100)
        drawing.write(description)
        drawing.goto(x_cord, y_cord)
        drawing.pendown()
        return drawing
    else:
        drawing.goto(x_cord, y_cord + 150)
        drawing.write(structure, font=("Arial", 25, "bold"))
        drawing.goto(x_cord, y_cord + 100)
        drawing.write(description)
        drawing.goto(x_cord, y_cord)
        drawing.pendown()
        return drawing





def arrow(drawing: turtle.Turtle, width: int,  direction='left'):
    size = width / 4
    if direction == 'left':
        drawing.forward(size * 3)  # line
        drawing.goto(drawing.xcor(), drawing.ycor() + (size/2))
        drawing.goto(drawing.xcor() - size, drawing.ycor() - (size/2))
        drawing.goto(drawing.xcor() + size, drawing.ycor() - (size/2))
        drawing.goto(drawing.xcor(), drawing.ycor() + (size/2))
        drawing.goto(drawing.xcor() + (size*3), drawing.ycor())
    elif direction == 'right':
        drawing.forward(size * 3)  # line
        drawing.goto(drawing.xcor(), drawing.ycor() + (size / 2))
        drawing.goto(drawing.xcor() + size, drawing.ycor() - (size / 2))
        drawing.goto(drawing.xcor() - size, drawing.ycor() - (size / 2))
        drawing.goto(drawing.xcor(), drawing.ycor() + (size / 2))
        drawing.goto(drawing.xcor() - (size*3), drawing.ycor())


def square(drawing: turtle.Turtle, height: int, rotation='right', width=None):
    if width is None:
        width = height
    if rotation == 'right':
        drawing.forward(width)
        drawing.right(90)
        drawing.forward(height)
        drawing.right(90)
        drawing.forward(width)
        drawing.right(90)
        drawing.forward(height)
    else:
        drawing.forward(width)
        drawing.left(90)
        drawing.forward(height)
        drawing.left(90)
        drawing.forward(width)
        drawing.left(90)
        drawing.forward(height)


def write_text(drawing: turtle.Turtle, data, height: int, rotation='right', align='center'):
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

def write_text_offset(drawing: turtle.Turtle, data, height: int, rotation='right', align='center'):
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
        drawing.forward(height*3)
        drawing.left(90)
        drawing.forward(height)
        drawing.write(data, False, align=align)
        drawing.left(90)
        drawing.forward(height*3)
        drawing.left(90)
        drawing.forward(height*3)
        drawing.pendown()