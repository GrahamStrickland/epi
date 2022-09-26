#!/usr/bin/env python3


from nose.tools import assert_equal
from ..spiral_ordering import matrix_in_spiral_order


def test_matrix_in_spiral_order() -> None:
    square_matrix = [[1,2,3],
                     [4,5,6],
                     [7,8,9]]
    obs = matrix_in_spiral_order(square_matrix)
    exp = [1,2,3,6,9,8,7,4,5]
    assert_equal(obs, exp)


def test_matrix_in_spiral_order2() -> None:
    square_matrix = [[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,15,16]]
    obs = matrix_in_spiral_order(square_matrix)
    exp = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
    assert_equal(obs, exp)
