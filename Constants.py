# screen setup
SCREEN_X, SCREEN_Y = 800, 700

# rectangle setup
ULR_X, ULR_Y, ULR_WIDTH, ULR_HEIGHT = -350, 300, 300, 500 # upper left
URR_X, URR_Y, URR_WIDTH, URR_HEIGHT = -30, 300, 250, 500 # upper right
PEN_SIZE, PEN_COLOR = 2, "blue" # upper right
LR_X, LR_Y, LR_WIDTH, LR_HEIGHT = - 350, - 220 , 570, 100 # lower

# button setup
CHECK_GIF, CHECK_X, CHECK_Y, CHECK_SIZE = "checkbutton.gif", 0, -270, 60
RESET_GIF, RESET_X, RESET_Y = "xbutton.gif", 80, -270
QUIT_GIF, QUIT_X, QUIT_Y = "quit.gif", 160, -270
BUTTON_SIZE = 15

# Leader board setup
LEADER_X, LEADER_Y = 50, 260
PLAYER_X, PLAYER_Y, LEADER_SPACE = 0, 220, 20

# Marble setup
MARBLE_RADIUS = 15
COLORS = ["red", "blue", "green", "yellow", "purple", "black"]
GUESS_X, GUESS_Y = -300, 250 # start coordinate of guess circle
RESULT_X, RESULT_Y = -100, 265 # start coordinate of result circle
STANDARD_X, STANDARD_Y = -300, -270 # start coordinate of standard circle
ROWS_GUESS, COLUMNS_GUESS = 10, 4 # guess 10 times, 4 colors each time
ROWS_RESULT, COLUMNS_RESULT = 2, 2 # result of bulls and cows 

# red mark setup
MARK_X, MARK_Y = -325, 265

# message setup
QUITMSG_GIF, WINMSG_GIF, LOSEMSG_GIF, ERROR_GIF = \
             "quitmsg.gif", "winner.gif", "lose.gif", "leaderboard_error.gif"
MSG_X, MSG_Y = 0, 30

# file setup
LEADER_FILE, ERROR_FILE = "leaderboard.txt", "mastermind_errors.err"
