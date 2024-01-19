#!/usr/bin/env python3


from nose.tools import assert_equal
from .gcd import gcd


def test_gcd() -> None:
    x, y = 156, 36
    obs = gcd(x,y)
    exp = 12
    assert_equal(obs, exp)


def test_gcd1() -> None:
    x, y = 1, 36
    obs = gcd(x,y)
    exp = 1
    assert_equal(obs, exp)


def test_gcd2() -> None:
    x, y = 150, 150
    obs = gcd(x,y)
    exp = 150
    assert_equal(obs, exp)
