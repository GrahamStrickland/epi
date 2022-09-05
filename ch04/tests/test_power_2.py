#! /usr/bin/env python3


from nose.tools import assert_equal
from ..power_2 import power_2


def test_power_2() -> None:
    x = 3
    exp = False
    obs = power_2(x)
    assert_equal(exp, obs)


def test_power_2_2() -> None:
    x = 4
    exp = True
    obs = power_2(x)
    assert_equal(exp, obs)


def test_power_2_3() -> None:
    x = 16
    exp = True
    obs = power_2(x)
    assert_equal(exp, obs)
    

def test_power_2_4() -> None:
    x = 0
    exp = True
    obs = power_2(x)
    assert_equal(exp, obs)


def test_power_2_5() -> None:
    x = 2123421341
    exp = False
    obs = power_2(x)
    assert_equal(exp, obs)