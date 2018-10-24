import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

# p1 = Point()
#
# p1.x = 3
# p1.y = 4
#
# p2 = Point()
#
# p2.x = 4
# p2.y = 5


def print_point(p):
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) **2)

# print(distance_between_points(p1, p2))

class Line:
    """Represents a line.

    attributes: pt1, pt2.
    """

class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """

# rect = Rectangle()
# rect.width = 100
# rect.height = 200
# rect.corner = p1


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

# print_point(find_center(rect))


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight
    return rect



def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)

def get_rectangle_points(rect):
    top_left = Point()
    top_left.x = rect.corner.x
    top_left.y = rect.corner.y + rect.height
    bottom_right = Point()
    bottom_right.x = rect.corner.x + rect.width
    bottom_right.y = rect.corner.y
    top_right = Point()
    top_right.x = rect.corner.x + rect.width
    top_right.y = rect.corner.y + rect.height
    return [ rect.corner, top_left, top_right, bottom_right ]

def get_rectangle_lines(rect):
    rect_points = get_rectangle_points(rect)
    rect_lines = []
    for index, point in enumerate(rect_points):
        line = Line()
        line.pt1 = rect_points[index - 1]
        line.pt2 = point
        rect_lines.append(line)
    return rect_lines


# print_rectangle(grow_rectangle(rect, 50, 100))

class Circle:
    """Represents a circle.

    attributes: center, radius.
    """

def point_in_circle(circle, point):
    return circle.radius >= distance_between_points(point, circle.center)

def rect_in_circle(rect, circle):
    rect_points = get_rectangle_points(rect)
    for point in rect_points:
        if not point_in_circle(circle, point):
            return False
    return True

def rect_circle_overlap(rect, circle):
    rect_lines = get_rectangle_lines(rect)
    for line in rect_lines:
        x_step = (line.pt2.x - line.pt1.x) / 100
        y_step = (line.pt2.y - line.pt1.y) / 100
        for i in range(100):
            point = Point()
            point.x = line.pt1.x + (x_step * i)
            point.y = line.pt1.y + (y_step * i)
            if point_in_circle(circle, point):
                return True
    return False

def main():
    # my_point = Point()
    # print(Point.__doc__)
    # my_point.x = 3
    # my_point.y = 4
    # print('My point', end=' ')
    # print_point(my_point)
    #
    # print('Is my_point an instance of Point?', isinstance(my_point, Point))
    # print('Is my_point an instance of Rectangle?',
    #       isinstance(my_point, Rectangle))
    # print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    # print('Does my_point have an attribute z?', hasattr(my_point, 'z'))
    #
    # box = Rectangle()
    # box.width = 100.0
    # box.height = 200.0
    # box.corner = Point()
    # box.corner.x = 0.0
    # box.corner.y = 0.0
    #
    # print('Does box have an attribute x?', hasattr(box, 'x'))
    #
    # print('Does box have an attribute corner?', hasattr(box, 'corner'))
    #
    # print('Rectangle has these:', dir(box))
    #
    # center = find_center(box)
    # print('center', end=' ')
    # print_point(center)
    #
    # print(box.width)
    # print(box.height)
    # print('grow')
    # grow_rectangle(box, 50, 100)
    # print(box.width)
    # print(box.height)

    p1 = Point()
    p1.x = 0
    p1.y = 0
    circle = Circle()
    circle.center = p1
    circle.radius = 10
    p2 = Point()
    p2.x = 9
    p2.y = -10
    print(point_in_circle(circle, p2))
    rect = Rectangle()
    rect.corner = p2
    rect.width = 10
    rect.height = 20
    print(rect_circle_overlap(rect, circle))


if __name__ == '__main__':
    main()
