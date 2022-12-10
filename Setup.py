import turtle
import time
from datetime import datetime
from Gif import Gif
from Rectangle import Rectangle
from Marble import Marble
from Leader import Leader
from Point import Point
from Constants import *

class Setup:
    """
        Setup class is the setup part of Mastermind.
        Setup class have attributes: pen, screen, name, leader, button,
    marble_standard, marble_guess, marble_result, msg.
        Setup class have methods: get_click, guess_color, count_bulls_and_cows,
    save_leader, check.
    """  
    def __init__(self):
        """
        Method:
            Create a new Setup instance with attributes: pen, screen, name,
        answer, leader, button, marble_standard, marble_guess, marble_result,
        msg.
        """        
        self.screen = self.screen_setup() # setup screen
        self.name = self.name_setup() # user name
        self.rectangle_setup() # draw 3 rectangles
        self.msg = self.msg_setup() # message gif dictionary
        self.leader = self.leader_setup(LEADER_FILE, ERROR_FILE) # leader list
        self.button = self.button_setup() # button gif dictionary
        self.marble_standard = self.marble_standard_setup() # 6 colored marbles
        self.pen = self.red_mark() # red mark
        # 4 * 10 guessing marbles and corresponding result marbles
        self.marble_guess, self.marble_result = self.marble_setup()

    def screen_setup(self):
        """
        Method: Create a screen with setup size.
        Return: turtle screen
        """                
        screen = turtle.Screen()
        screen.setup(SCREEN_X, SCREEN_Y) # setup screen size
        return screen

    def name_setup(self):
        """
        Method: Create a window to get user input.
        Return: user name
        """                        
        return self.screen.textinput("CS5001 MarsterMind", "Your name")

    def rectangle_setup(self):
        """
        Method: draw 3 rectangles.
        """
        Rectangle(Point(ULR_X, ULR_Y), ULR_WIDTH, ULR_HEIGHT).draw()
        Rectangle(Point(URR_X, URR_Y), URR_WIDTH, URR_HEIGHT,
                  PEN_SIZE, PEN_COLOR).draw()
        Rectangle(Point(LR_X, LR_Y), LR_WIDTH, LR_HEIGHT).draw()

    def msg_setup(self):
        """
        Method: generate Gif instances of message
        Return: message dictionary
        """                             
        msg = {} # message dictionary
        msg["win"] = Gif(self.screen, Point(MSG_X, MSG_Y), WINMSG_GIF)
        msg["quit"] = Gif(self.screen, Point(MSG_X, MSG_Y), QUITMSG_GIF)
        msg["lose"] = Gif(self.screen, Point(MSG_X, MSG_Y), LOSEMSG_GIF)
        msg["error"] = Gif(self.screen, Point(MSG_X, MSG_Y), ERROR_GIF)
        return msg

    def leader_setup(self, leader_file, error_file):
        """
        Method: try load leader file and handle exceptions
        Parameters:
            leader_file: file that saves leader information
            error_file: file that saves error information
        Return: nested list of leader 
        """                                        
        try:
            leader = self.load_file(leader_file) # get leader list from file
        except FileNotFoundError: # handle exception
            leader = [] # default with empty leader list
            self.msg["error"].draw() # error message
            time.sleep(3) # wait 3s
            self.msg["error"].pen.hideturtle()
            self.save_error(error_file) # save in error file
        return leader

    def load_file(self, leader_file):
        """
        Method:
            Load leader file return all leaders in a nested list, draw 10 best
        players on leader board.
        Parameter:
            leader_file: file name that saves leader information
        """                                        
        Leader(Point(LEADER_X, LEADER_Y), "Leader", 20).draw()
        leader, i = [], 0
        with open(leader_file, "r") as file:
            for line in file:
                leader.append(line.strip().split(" : ")) # all winners in list
                if i < 10: # display best 10 player
                    Leader(Point(PLAYER_X, PLAYER_Y - i * LEADER_SPACE),
                           line, 15).draw() # draw leader board
                    i += 1
        return leader # all leaders name and times in a nested list

    def save_error(self, error_file):
        """
        Method: save error file
        Parameters: error_file which saves error information
        """                                     
        with open(error_file, "a") as file:
            sentence = str(datetime.now()) + ": Could not find " + LEADER_FILE
            file.write(sentence + "\n") # save time and file name in error file

    def button_setup(self):
        """
        Method: generate Gif instances of button
        Return: button dictionary
        """                                
        button = {} # button dictionary
        button["check"] = Gif(self.screen, Point(CHECK_X, CHECK_Y), CHECK_GIF)
        button["reset"] = Gif(self.screen, Point(RESET_X, RESET_Y), RESET_GIF)
        button["quit"] = Gif(self.screen, Point(QUIT_X, QUIT_Y), QUIT_GIF)
        button["check"].draw() # draw all buttons
        button["reset"].draw()
        button["quit"].draw()
        return button

    def marble_standard_setup(self):
        """
        Method:
            generate Marble instances of 6 standard marbles, draw marbles
        and return standard marbles.
        Return:
            marble_standard: list of 6 marbles in lower rectrangle
        """            
        marble_standard = [] # 6 colored marbles
        for i in range(len(COLORS)):
            x_coor = STANDARD_X + i * 3 * MARBLE_RADIUS
            y_coor = STANDARD_Y       
            marble_standard.append(
                Marble(Point(x_coor, y_coor), MARBLE_RADIUS, COLORS[i]))
            marble_standard[i].draw() # draw standard marbles    
        return marble_standard
    
    def marble_setup(self):
        """
        Method:
            generate Marble instances of guess and result marbles, draw empty
        marbles and return marble lists
        Return:
            marble_guess: a nested list of 10*4 marbles for user to guess
            marble_result: a nested list of 10*4 marbles that show result
        """                    
        marble_guess, marble_result = [], []
        for i in range(ROWS_GUESS): # generate row by row
            marble_guess.append([])
            marble_result.append([])
            for j in range(COLUMNS_GUESS): # generate column by column
                x_coor = GUESS_X + j * 3 * MARBLE_RADIUS
                y_coor = GUESS_Y - i * 3 * MARBLE_RADIUS
                marble_guess[i].append(Marble(Point(x_coor, y_coor)))
                marble_guess[i][j].draw_empty() # draw guess marbles
            for k in range(ROWS_RESULT): # 2 upper marbles
                for h in range(COLUMNS_RESULT): # 2 lower marbles
                    x_coor = RESULT_X + h * MARBLE_RADIUS
                    y_coor = RESULT_Y - (i * 3 + k) * MARBLE_RADIUS
                    marble_new = Marble(Point(x_coor, y_coor),
                                        MARBLE_RADIUS / 3)
                    marble_result[i].append(marble_new)
                    marble_new.draw_empty() # draw result marbles
        return marble_guess, marble_result
    
    def red_mark(self):
        """
        Method:
            generate a new turtle and poit to starting row.
        Return:
            pen: red mark turtle
        """                    
        pen = turtle.Turtle()
        pen.color("red") # red mark turtle showing current row
        pen.up()
        pen.goto(MARK_X, MARK_Y)
        pen.speed(0)
        return pen

        
    
