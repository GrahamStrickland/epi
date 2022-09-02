#! /usr/bin/env python3


from nose.tools import assert_equal
from ..power_2 import test_power_2


def test_test_power_2() -> None:
    x = 3
    exp = False
    obs = test_power_2(x)
    assert_equal(exp, obs)