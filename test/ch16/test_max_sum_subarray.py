#!/usr/bin/env python3


from nose.tools import assert_equal
from .max_sum_subarray import find_maximum_subarray


def test_find_maximum_subarray() -> None:
    A = [904,40,523,12,-335,-385,-124,481,-31]
    obs = find_maximum_subarray(A)
    exp = 1479
    assert_equal(obs, exp)


def test_find_maximum_subarray1() -> None:
    A = [-2,3,1,-1,3,2,-1]
    obs = find_maximum_subarray(A)
    exp = 8
    assert_equal(obs, exp)
