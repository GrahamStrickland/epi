#!/usr/bin/env python3


from nose.tools import assert_equal

from .two_sum import has_two_sum


def test_has_two_sum() -> None:
    A = [-2, 1, 2, 4, 7, 11]
    obs = has_two_sum(A, 6)
    exp = True
    assert_equal(obs, exp)


def test_has_two_sum1() -> None:
    A = [-2, 1, 2, 4, 7, 11]
    obs = has_two_sum(A, 10)
    exp = False
    assert_equal(obs, exp)


def test_has_two_sum2() -> None:
    A = [-2, 1, 2, 4, 7, 11]
    obs = has_two_sum(A, 0)
    exp = True
    assert_equal(obs, exp)


def test_has_two_sum3() -> None:
    A = [-2, 1, 2, 4, 7, 11]
    obs = has_two_sum(A, 13)
    exp = True
    assert_equal(obs, exp)
