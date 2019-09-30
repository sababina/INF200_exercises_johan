# -*- coding: utf-8 -*-


__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


def char_counts(textfilename):
    """ Opens the given file then reads it in to single string.
    It then counts how often each character code occurs in the string, then
    returns a list with the results.

    Parameters
    ----------
    textfilename - The text file you want to analyse.

    Returns
    -------
    result - Returns a list of the counted character codes.
    """

    with open(textfilename, encoding='utf-8') as file:
        read_file = file.read()
        result = [0]*256

        for char in read_file:
            ascii_val = ord(char)
            result[ascii_val] += 1

    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
