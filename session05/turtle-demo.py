import turtle
import math

def polyline(t, n, length, angle):
    """
    Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """
    for i in range(n):
        if length > 0:
            t.fd(length)
        else:
            t.fd(-length)
        if angle > 0:
            t.lt(angle)
        else:
            t.rt(-angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(abs(arc_length) / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def elongated_arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(abs(arc_length) / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length / 3.05, step_angle / 4)

def circle(t, r):
    arc(t, r, 360)

def return_to_center(t, r):
    t.pu()
    t.sety(r)
    t.setx(0)
    t.pd()

def draw_petals(t, r, n):
    rotate = 360 / n
    for i in range(n):
        elongated_arc(t, r, 180)
        return_to_center(t, r)
        elongated_arc(t, r, -180)
        return_to_center(t, r)
        t.seth(t.heading() + rotate)

def flower(t, r):
    circle(t, r)
    return_to_center(t, r)
    draw_petals(t, r, 6)

def yin_yang(t, r):
    circle(t, r)
    arc(t, r / 2, 180)
    arc(t, r / 2, -180)
    t.pu()
    t.sety(t.ycor() - (r / 2) - (r / 8))
    t.pd()
    circle(t, r / 8)
    t.pu()
    t.sety(t.ycor() - r)
    t.pd()
    circle(t, r / 8)

def circle_with_triangles(t, r):
    circle(t, r)
    t.pu()
    t.sety(t.ycor() + (r / 2.4) - (r / 3.5))
    t.pd()
    circle(t, r / 3.5)
    t.pu()
    t.sety(t.ycor() - (r / 2.4) + (2 * r) - (r / 2.4))
    t.pd()
    circle(t, r / 3.5)
    return_to_center(t, r)
    t.pu()
    t.sety(t.ycor() - r / 3.5)
    t.setx(t.xcor() + r - r / 2.4)
    t.pd()
    circle(t, r / 3.5)
    t.pu()
    t.setx(t.xcor() + (r / 2.4) - (2 * r) + (r / 2.4))
    t.pd()
    circle(t, r / 3.5)
    return_to_center(t, r)
    t.seth(60)
    polyline(t, 3, r, 120)
    t.seth(150)
    polyline(t, 3, r, 120)
    t.seth(240)
    polyline(t, 3, r, 120)
    t.seth(330)
    polyline(t, 3, r, 120)

# yin_yang(turtle.Turtle(), 120)
# flower(turtle.Turtle(), 100)
circle_with_triangles(turtle.Turtle(), 100)


turtle.mainloop()
