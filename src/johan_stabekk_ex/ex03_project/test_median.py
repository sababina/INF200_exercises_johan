# -*- coding: utf-8 -*-

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'

import statistics
import pytest


def median(data):
    """
    Returns median of data in a new version that makes the ValueError test
    work.

    This function was made by Yngve in the lecture. I modified it a bit by
    including elif to raise ValueError so that the test that raises
    ValueError works.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    elif not sorted_data:
        raise ValueError('Please insert a list that is not empty')
    else:
        return (
            sorted_data[num_elements // 2 - 1] + sorted_data[num_elements // 2]
        ) / 2


def test_median_of_singleton():
    assert median([4]) == 4


def test_median_of_odd_numbers():
    data = [1, 3, 5, 7, 9]
    assert median(data) == statistics.median(data)


def test_median_of_even_numbers():
    data = [2, 4, 6, 8, 10]
    assert median(data) == statistics.median(data)


def test_median_of_ordered_list():
    data = [1, 2, 3, 4, 5]
    assert median(data) == statistics.median(data)


def test_median_of_reverse_ordered_list():
    data = [5, 4, 3, 2, 1]
    assert median(data) == statistics.median(data)


def test_median_of_unordered_list():
    data = [3, 5, 2, 1, 4]
    assert median(data) == statistics.median(data)


def test_median_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_original_data_stays_same():
    data = [1, 2, 3, 4, 5, 6]
    median(data)
    assert data == [1, 2, 3, 4, 5, 6]


def test_median_of_tuple_works():
    list1 = [1, 2, 3, 4]
    tuple1 = tuple(list1)
    assert median(tuple1) == median(list1)
