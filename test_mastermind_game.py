"""
    Conghui Sun
    CS5001 Spring 2022
    Project Mastermind test
    Create a MastermindTest class that tests function: 1) answer_setup,
2) count_bulls_and_cows.
"""

ANSWER = [["red", "blue", "green", "black"],
          ["yellow", "red", "green", "black"],
          ["black", "green", "blue", "red"],
          ["green", "red", "black", "purple"],
          ["purple", "blue", "red", "green"]]
GUESS = [["yellow", "yellow", "yellow", "yellow"],
         ["red", "green", "black", "yellow"],
         ["black", "green", "blue", "red"],
         ["green", "red", "purple", "black"],
         ["purple", "red", "green", "black"]]
COWS = [0, 4, 0, 2, 2]
BULLS = [0, 0, 4, 2, 1]

import unittest
from secret_code import *

class MastermindTest(unittest.TestCase):
    """
        Test class to test function that generating answer and
    counting bulls and cows.
    """
    def test_answer_setup(self):  # Test function answer_setup
        answer1, answer2 = answer_setup(), answer_setup()
        # 1) length is 4
        self.assertEqual(len(answer1), 4)
        # 2) no repeats
        self.assertEqual(len(set(answer1)) == len(answer1), True)
        # 3) choose from given colors
        self.assertEqual(set(answer1) < set(COLORS), True)
        # 4) choose randomly
        self.assertEqual(answer1 == answer2, False)
        
    def test_count_bulls_and_cows(self): # Test function count_bulls_and_cows
        for i in range(len(ANSWER)): # test different scores of bulls and cows
            self.assertEqual(count_bulls_and_cows(ANSWER[i], GUESS[i])
                             == (COWS[i], BULLS[i]), True)

def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
