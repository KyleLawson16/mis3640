import turtle
import math

def polygon(shape, sides, length):
    '''
    Draw a polygon with # of sides, and length of side
    '''
    for i in range(sides):
        shape.fd(length)
        shape.lt(360 / sides)

# polygon(turtle.Turtle(), 7, 50)

def circle(shape, r):
    circumference = math.pi * 2 * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(shape, n, length)

# circle(turtle.Turtle(), 100)

def arc(shape, r, angle):
    circumference = math.pi * 2 * r
    n = int(circumference / 3) + 1
    n_arc  = round((angle / 360) * n)
    length = circumference / n
    for i in range(n_arc):
        shape.fd(length)
        shape.lt(360 / n)

arc(turtle.Turtle(), 50, 120)

turtle.mainloop()
