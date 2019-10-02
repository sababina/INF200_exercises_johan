# -*- coding: utf-8 -*-

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'

import statistics
import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
            else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


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

