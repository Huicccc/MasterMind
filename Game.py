import time
from Setup import Setup
from Constants import *
from secret_code import *

class Game:
    """
        Game class have attributes: pen, screen, row, column, name,
    leader, button, marble_standard, marble_guess, marble_result, msg.
        Game class have methods: __init__, get_click, guess_color,
    count_bulls_and_cows, save_leader, check.
        The class is the strategy part of Mastermind.
    """  
    def __init__(self, pen, screen, name, leader, button,
                 marble_standard, marble_guess, marble_result, msg):
        """
        Method:
            Create a new Game instance by supplying pen, screen, name,
        leader, button, marble_standard, marble_guess, marble_result, msg.
        Parameters:
            pen: turtle pen which shows as red mark
            screen: screen attribute of instance of class Setup
            position: instance of Position class
            name: user name
            answer: four colors answer list
            leader: nested list of all leader name and guessing times
            button: button dictionary
            marble_standard: 6 marbles in lower rectrangle
            marble_guess: a nested list of 10*4 marbles for user to guess
            marble_result: a nested list of 10*4 marbles that show result
            msg: message dictionary
        """
        self.row = 0 # current row 0 - 9
        self.column = 0 # current column 0 - 3
        self.screen = screen # screen from instance of Class Setup
        self.name = name # user name
        self.answer = answer_setup() # generate answer
        self.leader = leader # leader list
        self.button = button # button dictionary
        self.marble_standard = marble_standard # list of 6 standard marbles
        self.marble_guess = marble_guess # nested list of guessing marbles
        self.marble_result = marble_result # nested list of result marbles
        self.msg = msg # message dictionary
        self.pen = pen # red mark showing current row
        self.check()

    def get_click(self, x, y):
        """
        Method:
            Method takes clicking position to generates strategy of next
        move, such as showing win or loss.
            Method includes funtion: guess_color, count_bulls_and_cows, and
        save_leader.
        Parameters:
            x: x coordinate of clicking
            y: y coordinate of clicking
        """        
        # 1. quit: click quit button, show message, close window in 3s
        if self.button["quit"].clicked_in_region(x, y, BUTTON_SIZE): # click
            self.msg["quit"].draw() # draw gif
            self.close_window() # close window in 2s
            
        # 2. reset: click reset button, reset marbles in current row
        elif self.button["reset"].clicked_in_region(x, y, BUTTON_SIZE) and \
             self.column != 0: # reset when guess more than one color
            for i in range(COLUMNS_GUESS): # redraw 4 guessing marbles
                self.marble_guess[self.row][i].draw_empty()
            for i in range(len(COLORS)): # redraw 6 standard marbles
                self.marble_standard[i].draw()
            self.column = 0 # reset current column
            
        # 3. check: after four guesses and click check button
        elif self.button["check"].clicked_in_region(x, y, BUTTON_SIZE) and \
            self.column == COLUMNS_GUESS: # check only after 4 guesses
            self.column = 0 # column restart from 0
            for i in range(len(COLORS)): # reset 6 standard marbles
                self.marble_standard[i].draw()                      
            color_list = self.get_guess_color() # get 4 result colors
            # calcute cows and bulls
            cows, bulls = count_bulls_and_cows(color_list, self.answer)
            self.draw_bulls_and_cows(cows, bulls) # draw result marbles
            # 3.1 win the game
            if bulls == COLUMNS_GUESS: # 4 bulls
                self.msg["win"].draw() # draw win gif
                self.leader.append([self.name, self.row + 1]) # append leader
                self.save_leader(LEADER_FILE) # save all leaders into file
                self.close_window() # close window in 2s
            # 3.2 lose the game
            elif self.row + 1 == ROWS_GUESS: # 10 guesses
                self.msg["lose"].draw() # draw lose gif
                time.sleep(2) # show answer after 2s
                self.screen.textinput("ANSWER", (" ").join(self.answer))
                self.close_window() # close window in 2s
            # 3.3 continue the game
            else:
                self.row += 1 # move to next row
                # red mark move to next row
                self.pen.goto(MARK_X, MARK_Y - self.row * 3 * MARBLE_RADIUS)
                
        # 4. guess: click on standard marbles to guess color
        else:
            if self.column < COLUMNS_GUESS: # less than 4 guesses
                if self.guess_color(x, y) == True: # draw color of guess marble
                    self.column += 1 # move to next column
       
    def guess_color(self, x, y):
        """
        Method:
            Method takes clicking position to draw color on guessing marble.
        Parameters:
            x: x coordinate of clicking
            y: y coordinate of clicking
        Return:
            True: Successfully draw the marble.
        """         
        for i in range(len(COLORS)): # iterate 6 standard marbles
            if self.marble_standard[i].clicked_in_region(x, y) and \
               self.marble_standard[i].is_empty == False: # color not used
                new_color = self.marble_standard[i].get_color() # get new color
                self.marble_standard[i].draw_empty() # redraw standard marble
                # set new color to current guess marble and redraw marble
                self.marble_guess[self.row][self.column].set_color(new_color)
                self.marble_guess[self.row][self.column].draw()
                return True

    def get_guess_color(self):
        """
        Method: generate guess color list.
        """        
        color_list = [] # empty result color list
        for i in range(COLUMNS_GUESS): # get color from current guessing row
            color_list.append(self.marble_guess[self.row][i].get_color())
        return color_list
            

    def draw_bulls_and_cows(self, cows, bulls):
        """
        Method: draw result marbles with given cows and bulls.
        """        
        for i in range(bulls): # draw black balls in current row
            self.marble_result[self.row][i].set_color("black")
            self.marble_result[self.row][i].draw()
        for i in range(bulls, bulls + cows): # draw red balls in current row
            self.marble_result[self.row][i].set_color("red")
            self.marble_result[self.row][i].draw()        

    def save_leader(self, leader_file):
        """
        Method:
            Method saves leader information in leader_file. 
        Parameter:
            leader_file: file that saves leader information.
        """
        # rank leader based on trying times from smallest to largest
        self.leader = sorted(self.leader, key = lambda x: int(x[1]))
        with open(leader_file, "w") as file: # save all leaders into file
            for i in range(len(self.leader)):
                sentence = (" : ").join([self.leader[i][0], str(self.leader[i][1])])
                file.write(sentence + "\n")

    def close_window(self):
        """
        Method: sleep 2s and close window
        """
        time.sleep(2) # sleep 2s
        self.screen.bye() # close window
        
    def check(self):
        """
        Method: execute onclick function
        """        
        self.screen.onclick(self.get_click)
