#! /usr/bin/env python3


from nose.tools import assert_equal
from ..longest_subarray_equal import longest_subarray_equal


def test_longest_subarray_equal() -> None:
    A = [1, 2, 4, 5, 12, 12, 12, 7, 9, 10, 10, 35]
    exp = 3
    obs = longest_subarray_equal(A)
    assert_equal(exp, obs)


def test_longest_subarray_equal2() -> None:
    A = range(100)
    exp = 1
    obs = longest_subarray_equal(A)
    assert_equal(exp, obs)


def test_longest_subarray_equal3() -> None:
    A = 10 * [1]
    exp = 10
    obs = longest_subarray_equal(A)
    assert_equal(exp, obs)


def test_longest_subarray_equal4() -> None:
    A = [1, 4, 4, 4, 4, 1]
    exp = 4
    obs = longest_subarray_equal(A)
    assert_equal(exp, obs)


def test_longest_subarray_equal5() -> None:
    A = [7, 7, 7, 7, 7, 7 , 2, 7, 7, 7, 7, 7]
    exp = 6
    obs = longest_subarray_equal(A)
    assert_equal(exp, obs)


def test_longest_subarray_equal6() -> None:
    A = [7, 7, 7, 7, 7, 2, 7, 7, 7, 7, 7, 7]
    exp = 6
    obs = longest_subarray_equal(A)
    assert_equal(exp, obs)