#!/usr/bin/env python3


from nose.tools import assert_equal
from ..kth_largest_in_array import find_kth_largest


def test_find_kth_largest0() -> None:
    k = 1
    A = [3,1,-1,2]
    obs = find_kth_largest(k, A)
    exp = 3
    assert_equal(obs, exp)
    
    
def test_find_kth_largest1() -> None:
    k = 2
    A = [3,1,-1,2]
    obs = find_kth_largest(k, A)
    exp = 2
    assert_equal(obs, exp)


def test_find_kth_largest2() -> None:
    k = 3
    A = [3,1,-1,2]
    obs = find_kth_largest(k, A)
    exp = 1
    assert_equal(obs, exp)


def test_find_kth_largest3() -> None:
    k = 4
    A = [3,1,-1,2]
    obs = find_kth_largest(k, A)
    exp = -1
    assert_equal(obs, exp)


def test_find_kth_largest4() -> None:
    k = 1
    A = [3,2,1,5,4]
    obs = find_kth_largest(k, A)
    exp = 5
    assert_equal(obs, exp)


def test_find_kth_largest5() -> None:
    k = 2
    A = [3,2,1,5,4]
    obs = find_kth_largest(k, A)
    exp = 4
    assert_equal(obs, exp)


def test_find_kth_largest6() -> None:
    k = 3
    A = [3,2,1,5,4]
    obs = find_kth_largest(k, A)
    exp = 3
    assert_equal(obs, exp)


def test_find_kth_largest7() -> None:
    k = 4
    A = [3,2,1,5,4]
    obs = find_kth_largest(k, A)
    exp = 2
    assert_equal(obs, exp)


def test_find_kth_largest8() -> None:
    k = 5
    A = [3,2,1,5,4]
    obs = find_kth_largest(k, A)
    exp = 1
    assert_equal(obs, exp)
