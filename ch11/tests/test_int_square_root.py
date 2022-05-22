#!/usr/bin/env python3


from nose.tools import assert_equal
from ..int_square_root import square_root


def test_square_root0() -> None:
    k = 16
    obs = square_root(16)
    exp = 4
    assert_equal(obs, exp)


def test_square_root1() -> None:
    k = 300
    obs = square_root(k)
    exp = 17
    assert_equal(obs, exp)


def test_square_root2() -> None:
    k = 0
    obs = square_root(k)
    exp = 0
    assert_equal(obs, exp)


def test_square_root3() -> None:
    k = 1
    obs = square_root(k)
    exp = 1
    assert_equal(obs, exp)
