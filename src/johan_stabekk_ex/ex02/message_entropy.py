# -*- coding: utf-8 -*-


import numpy as np


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


def entropy(message):

    dist = letter_freq(message)
    su = 0
    for p in dist.values():
        r = p / sum(dist.values())
        if r == 0:
            su += 0
        else:
            su += -r * (np.log(r))
    return su / np.log(2)


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
