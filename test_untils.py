"""
File implements tests of utils.py
"""

import pytest
import utils


@pytest.mark.parametrize(
    "a , b , expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    """
    Tests add function
    :param a: First number as int
    :param b: Second number as int
    :param expected: Expected result as int
    :return: Result of summation as int
    """
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a , b , expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    """
    Tests subtracting function
    :param a: First number as int
    :param b: Second number as int
    :param expected: Expected result as int
    :return: Result of subtraction as int
    """
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a , b , expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    """
    Tests multiplication function
    :param a: First number as int
    :param b: Second number as int
    :param expected: Expected result as int
    :return: Result of multiplication as int
    """
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a , b , expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    """
    Tests division function
    :param a: First number as int
    :param b: Second number as int
    :param expected: Expected result as int
    :return: Result of division as int
    """
    result = utils.divide(a, b)
    assert result == expected
