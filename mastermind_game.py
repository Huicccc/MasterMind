"""
    Conghui Sun
    CS5001 Spring 2022
    Project: Mastermind Game
    Create a version of Mastermind for one player: program selects 4 colors,
the score is the number of guesses it takes the player to guess.
    The player loses if they don’t guess the code in 10 tries.
    Scoring pegs will be red for cows(correct guesses with incorrect positions)
and black for bulls(guesses with correct position).
"""
from Setup import Setup
from Game import Game

def main():
    setup = Setup()
    Game(setup.pen, setup.screen, setup.name, setup.leader, setup.button,
         setup.marble_standard, setup.marble_guess, setup.marble_result,
         setup.msg)

if __name__ == "__main__":
    main()
