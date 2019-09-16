from random import randint

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'

"""

"""


def get_valid_input():
    count = 0
    while count < 1:
        count = int(input('Your guess between 2 and 12: '))
    return count


def roll_dice():
    return randint(1, 6) + randint(1, 6)


def is_answer_correct(correct, guess):
    return correct == guess


if __name__ == '__main__':

    guessed_correct = False
    remaining_attempts = 3
    correct_answer = roll_dice()
    while not guessed_correct and remaining_attempts > 0:
        your_guess = get_valid_input()
        guessed_correct = is_answer_correct(correct_answer, your_guess)
        if not guessed_correct:
            print('Wrong, try again!')
            remaining_attempts -= 1

    if remaining_attempts > 0:
        print('You won {} points.'.format(remaining_attempts))
    else:
        print('You lost. Correct answer: {}.'.format(correct_answer))
