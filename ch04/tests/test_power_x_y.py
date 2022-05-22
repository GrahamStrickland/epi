#!/usr/bin/env python3


from nose.tools import assert_equal
from  ..power_x_y import power


def test_power0() -> None:
    x, y = 1.0, 1
    obs = power(x, y)
    exp = 1.0
    assert_equal(obs, exp)


def test_power1() -> None:
    x, y = 1.1, 21
    obs = power(x, y)
    exp =  7.400249944258171
    assert_equal(obs, exp)


def test_power2() -> None:
    x, y = -2.0, 2
    obs = power(x, y)
    exp =  4.0
    assert_equal(obs, exp)


def test_power3() -> None:
    x, y = 2.0, -2
    obs = power(x, y)
    exp =  0.25
    assert_equal(obs, exp)


def test_power4() -> None:
    x, y = 0.0, 10
    obs = power(x, y)
    exp =  0.0
    assert_equal(obs, exp)
