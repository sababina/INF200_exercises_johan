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


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data is not data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = sorted([3, 2, 1, 6, 10])
    assert bubble_sort(data) == [1, 2, 3, 6, 10]


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [5, 4, 3, 2, 1]
    sorted_data = sorted(data)
    assert bubble_sort(data) == sorted_data


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1]*5
    assert bubble_sort(data) == [1]*5


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """

    sorted_numbers_int = [3, 4, 5, 6, 7]
    assert bubble_sort(sorted_numbers_int) == sorted(sorted_numbers_int)

    sorted_string = ['abehasdfavehhe']
    assert bubble_sort(sorted_string) == sorted(sorted_string)

    sorted_string_list = ['aaa', 'bnbabbb', 'jfqgqefsjfjff']
    assert bubble_sort(sorted_string_list) == sorted(sorted_string_list)

    sorted_numbers_float = [0.0000, 0.89898, 0.9999]
    assert bubble_sort(sorted_numbers_float) == sorted(sorted_numbers_float)
