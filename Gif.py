import turtle
from Constants import BUTTON_SIZE
class Gif:
    """
        Rectangle class have attributes pen, color, size, position, height,
    width. The class can draw an rectangle requires the use of the class Point.
    """    
    def __init__(self, screen, position, gif):
        """
        Method:
            Create a new Gif instance by supplying position and gif name.
        Parameters:
            position: instance of Position class
            gif: name of gif
        """
        screen.addshape(gif) # add shape to the shape list
        self.pen = self.new_pen()
        self.position = position
        self.gif = gif
        self.pen.hideturtle()
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
        self.pen.showturtle()
        self.pen.shape(self.gif) # set turtle with new shape and new position

    def clicked_in_region(self, x, y, size = BUTTON_SIZE):
        """
        Method:
            Check whether click inside the GIF instance area.
        Parameters:
            x: x coordinate of click.
            y: y coordinate of click.
            size: parameter of button, default with BUTTON_SIZE
        Return:
            True: click inside the region
            False: click outside the region
        """        
        if abs(x - self.position.x) <= size * 2 and \
           abs(y - self.position.y) <= size * 2:
            return True
        return False
    
