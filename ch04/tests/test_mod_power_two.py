#! /usr/bin/env python3


from nose.tools import assert_equal
from ..mod_power_two import mod_power_two


def test_mod_power_two() -> None:
    x = 77
    a = 64
    exp = 13
    obs = mod_power_two(x, a)
    assert_equal(exp, obs)


def test_mod_power_two2() -> None:
    x = 77
    a = 32
    exp = 13
    obs = mod_power_two(x, a)
    assert_equal(exp, obs)


def test_mod_power_two3() -> None:
    x = 15
    a = 16
    exp = 15
    obs = mod_power_two(x, a)
    assert_equal(exp, obs)


def test_mod_power_two4() -> None:
    x = 60
    a = 16
    exp = 12
    obs = mod_power_two(x, a)
    assert_equal(exp, obs)


def test_mod_power_two5() -> None:
    x = 3
    a = 2
    exp = 1
    obs = mod_power_two(x, a)
    assert_equal(exp, obs)