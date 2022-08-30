#! /usr/bin/env python3


from nose.tools import assert_equal
from ..mod_power_two import mod_power_two


def test_mod_power_two() -> None:
    x = 77
    a = 64
    exp = 13
    obs = mod_power_two(x, a)
    assert_equal(exp, obs)