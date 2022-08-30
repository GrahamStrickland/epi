#! /usr/bin/env python3


from nose.tools import assert_equal
from ..right_propagate_bit import right_propagate_rightmost_bit


def test_right_propagate_rightmost_bit() -> None:
    x = 0b01010000
    exp = 0b01011111
    obs = right_propagate_rightmost_bit(x)
    assert_equal(bin(exp), obs)


def test_right_propagate_rightmost_bit1() -> None:
    x = 0b01000000
    exp = 0b01111111
    obs = right_propagate_rightmost_bit(x)
    assert_equal(bin(exp), obs)


def test_right_propagate_rightmost_bit2() -> None:
    x = 0b01010101
    exp = 0b01010101
    obs = right_propagate_rightmost_bit(x)
    assert_equal(bin(exp), obs)


def test_right_propagate_rightmost_bit3() -> None:
    x = 0b1
    exp = 0b1
    obs = right_propagate_rightmost_bit(x)
    assert_equal(bin(exp), obs)


def test_right_propagate_rightmost_bit4() -> None:
    x = 0b10
    exp = 0b11
    obs = right_propagate_rightmost_bit(x)
    assert_equal(bin(exp), obs)