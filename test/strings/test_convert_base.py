#!/usr/bin/env python3


from nose.tools import assert_equal

from ..convert_base import convert_base


def test_convert_base0() -> None:
    num_as_string = "615"
    b1 = 7
    b2 = 13
    obs = convert_base(num_as_string, b1, b2)
    exp = "1A7"
    assert_equal(obs, exp)


def test_convert_base1() -> None:
    num_as_string = "10101100"
    b1 = 2
    b2 = 10
    obs = convert_base(num_as_string, b1, b2)
    exp = "172"
    assert_equal(obs, exp)


def test_convert_base2() -> None:
    num_as_string = "FFFF"
    b1 = 16
    b2 = 2
    obs = convert_base(num_as_string, b1, b2)
    exp = "1111111111111111"
    assert_equal(obs, exp)
