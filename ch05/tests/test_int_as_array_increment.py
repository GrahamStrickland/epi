#! /usr/bin/env python3


from nose.tools import assert_equal
from ..int_as_array_increment import plus_one


def test_plus_one() -> None:
    D = [1, 2, 9]
    exp = [1, 3, 0]
    obs = plus_one(D)
    assert_equal(exp, obs)


def test_plus_one1() -> None:
    D = [9, 9, 9]
    exp = [1, 0, 0, 0]
    obs = plus_one(D)
    assert_equal(exp, obs)


def test_plus_one2() -> None:
    D = [9]
    exp = [1, 0]
    obs = plus_one(D)
    assert_equal(exp, obs)


def test_plus_one3() -> None:
    D = [0, 0, 0]
    exp = [0, 0, 1]
    obs = plus_one(D)
    assert_equal(exp, obs)


def test_plus_one4() -> None:
    D = [1, 9, 2]
    exp = [1, 9, 3]
    obs = plus_one(D)
    assert_equal(exp, obs)