# -*- coding: utf-8 -*-


__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


def char_counts(textfilename):
    """

    Parameters
    ----------
    textfilename

    Returns
    -------

    """

    with open(textfilename, encoding='utf-8') as file:
        read_file = file.read()
        result = [0]*256

        converted_file = [ord(char) for char in read_file]

        for val in range(len(read_file)):
            for char_nr in range(256):
                if converted_file[val] == char_nr:
                    result[char_nr] += 1

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
