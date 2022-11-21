#!/usr/bin/env python3


from nose.tools import assert_equal
from ..spiral_ordering2 import matrix_in_spiral_order


def test_matrix_in_spiral_order() -> None:
    square_matrix = [[1, 2, 3], 
                     [4, 5, 6], 
                     [7, 8, 9]]
    obs = matrix_in_spiral_order(square_matrix)
    exp = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert_equal(obs, exp)


def test_matrix_in_spiral_order2() -> None:
    square_matrix = [[1, 2, 3, 4], 
                     [5, 6, 7, 8], 
                     [9, 10, 11, 12], 
                     [13, 14, 15, 16]]
    obs = matrix_in_spiral_order(square_matrix)
    exp = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    assert_equal(obs, exp)


def test_matrix_in_spiral_order3() -> None:
    square_matrix = [[1, 2, 3, 4, 5], 
                     [6, 7, 8, 9, 10], 
                     [11, 12, 13, 14, 15], 
                     [16, 17, 18, 19, 20], 
                     [21, 22, 23, 24, 25]]
    obs = matrix_in_spiral_order(square_matrix)
    exp = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
    assert_equal(obs, exp)
