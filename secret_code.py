import random
from Constants import COLUMNS_GUESS, COLORS

def count_bulls_and_cows(color_list: str, answer: str):
    """
    Function:
        compare guess and answer, return cows and bulls.
    Parameters:
        color_list: guess color list
        answer: secrete code color list
    Return:
        cows(int): numbers of right color but wrong position
        bulls(int): numbers of right color and right position
    """
    bulls, cows = 0, 0
    for i in range(COLUMNS_GUESS):
        if answer[i] == color_list[i]:
            bulls += 1
        elif answer[i] in color_list:
            cows += 1
    return cows, bulls


def answer_setup() -> list:
    """
    Function:
        Random generate 4 colors.
    Return:
        A list of 4 colors. 
    """                                
    return random.sample(COLORS, k = COLUMNS_GUESS)
