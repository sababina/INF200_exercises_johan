# -*- coding: utf-8 -*-

import numpy as np

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


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
    """

    Parameters
    ----------
    message

    Returns
    -------

    """

    message = letter_freq(message)
    h = 0
    for n_i in message.values():
        p_i = n_i / sum(message.values())
        if p_i == 0:
            h += 0
        else:
            h += -p_i * (np.log(p_i))
    return h / np.log(2)


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
