

"""
Solution to  task C on exercise 01 in INF200
"""


def letter_freq(txt):
    pass


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))