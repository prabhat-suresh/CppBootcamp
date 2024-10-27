'''
    Author: Bhogaraju Shanmukha Sri Krishna
    Roll No: 112201013

    Maintaining modularity. Using functions from other files to run the game here
'''

from GameRunner import run
from WordParser import openFileAndGetWords

ALL_WORDS = openFileAndGetWords('../WordleAnswersList.txt')
MAX_CHANCES = 6

if __name__ == '__main__':
    run(MAX_CHANCES, ALL_WORDS)