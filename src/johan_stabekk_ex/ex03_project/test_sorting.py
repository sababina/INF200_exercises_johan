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
    empty_list = []
    assert bubble_sort(empty_list) == empty_list


def test_single():
    """Test that the sorting function works for single-element list"""
    single_list = [1]
    assert bubble_sort(single_list) == single_list


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
    assert sorted_data != data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert all(elem in data for elem in sorted_data)


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    pass


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass
