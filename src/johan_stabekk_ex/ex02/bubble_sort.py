# -*- coding: utf-8 -*-

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


def bubble_sort(data_):
    """ Sorts the data after the bubble_sort algorithm.

    Parameters
    ----------
    data_ - The data that is going to be sorted.

    Returns
    -------
    data_sorted - Returns the input data sorted in a new list.
    """
    data_sorted = list(data_)

    for i in range(len(data_sorted) - 1):
        for j in range(len(data_sorted) - 1 - i):
            if data_sorted[j] > data_sorted[j + 1]:
                data_sorted[j], data_sorted[j+1] = \
                    data_sorted[j+1], data_sorted[j]

    return data_sorted


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
