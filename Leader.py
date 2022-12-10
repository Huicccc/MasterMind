import turtle
from Point import Point
class Leader:
    """
        Leader class takes position, line and front size to draw leaders
    information in leader board.
    """    
    def __init__(self, position, line, size):
        """
        Method:
            Create a new Leader instance by supplying position, line and front
        size.
        Parameters:
            position: instance of Position class
            line: leader name and guessing times
            size: front size
        """        
        self.pen = self.new_pen()
        self.position = position
        self.pen.hideturtle()
        self.pen.speed(0)
        self.line = line.strip("/n")
        self.size = size

    def new_pen(self):
        """
        Method: Create a new turtle.
        Return: A new turtle.
        """               
        return turtle.Turtle()

    def draw(self):
        """
        Method:
            Draw players information from position with front size
        """               
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.color("blue")
        self.pen.write(self.line, move = False, align = "left", font =
                       ("Arial", self.size, "normal"))
