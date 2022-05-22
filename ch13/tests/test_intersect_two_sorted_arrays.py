#!/usr/bin/env python3


from nose.tools import assert_equal
from ..intersect_two_sorted_arrays import intersect_two_sorted_arrays


def test_intersect_two_sorted_arrays0():
    A = [2,3,3,5,5,6,7,7,8,12]
    B = [5,5,6,8,8,9,10,10]
    obs = intersect_two_sorted_arrays(A, B)
    exp = [5,6,8]
    assert_equal(obs, exp)


def test_intersect_two_sorted_arrays1():
    A = [1,1,1,1,1,1,1]
    B = [0]
    obs = intersect_two_sorted_arrays(A, B)
    exp = []
    assert_equal(obs, exp)


def test_intersect_two_sorted_arrays2():
    A = [2]
    B = [2,2,2,3,4,5,6]
    obs = intersect_two_sorted_arrays(A, B)
    exp = [2]
    assert_equal(obs, exp)


def test_intersect_two_sorted_arrays3():
    A = []
    B = [1,2,3,4,5]
    obs = intersect_two_sorted_arrays(A, B)
    exp = []
    assert_equal(obs, exp)
