# -*- coding: utf-8 -*-

from random import randint

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'

"""
This code is a guessing game where you have to guess a number between 2 and 12. 
You get points according to how many times you try.
You have three attempts.
"""


def get_valid_input():
    """
    This function gets a integer input from the player.
    :return: The input
    """
    count = 0
    while count < 1:
        count = int(input('Your guess between 2 and 12: '))
    return count


def roll_dice():
    """
    Simulates the rolling of who dices.
    :return: The sum of the two dices.
    """
    return randint(1, 6) + randint(1, 6)


def is_answer_correct(correct, guess):
    """
    This function checks if the players answer is correct
    :param correct: The correct answer
    :param guess: The players guess
    :return: Returns if the answer is true or false
    """
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
