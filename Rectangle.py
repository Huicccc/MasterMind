import turtle
class Rectangle:
    """
        Rectangle class have attributes pen, color, size, position, height,
    width. The class can draw an rectangle requires the use of the class Point.
    """
    def __init__(self, position, width, height, pen_size = 4, color = "black"):
        """
        Method:
            Create a new Rectangle instance by supplying position, width,
        height, pen_size with default 4, color with default "black".
        Parameters:
            position: instance of Position class
            width: the width of rectangle
            height: the height of rectangle
            pen_size: the size of pen
            color: the color of pen
        """
        self.pen = self.new_pen()
        self.color = color
        self.size = pen_size
        self.position = position
        self.pen.hideturtle()
        self.height = height
        self.width = width        
        self.pen.speed(0)

    def new_pen(self):
        """
        Method: Create a new turtle.
        Return: A new turtle.
        """
        return turtle.Turtle()

    def draw(self):
        """
        Method:
            Draw a rectangle starting from position with given width, height,
        pen size and color.
        """
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.color(self.color)
        self.pen.pensize(self.size)

        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.right(90)
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
