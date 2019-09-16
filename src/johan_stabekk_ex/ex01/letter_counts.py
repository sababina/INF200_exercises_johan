# -*- coding: utf-8 -*-

"""
Solution to  task C on exercise 01 in INF200
"""


def letter_freq(txt):
    """
    This code counts the frequency of how many times a character is used.
    :param txt: input for the user of the code.
    :return: Returns a dictionary where the frequency of characters in txt is placed, with the character as a key and
             the number of times as a value
    """
    freq = {}
    txt_lowered = txt.lower()

    for char in txt_lowered:
        if char in freq.keys():
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    frequencies_sorted = dict(sorted(frequencies.items()))

    for letter, count in frequencies_sorted.items():
        print('{:3}{:10}'.format(letter, count))
