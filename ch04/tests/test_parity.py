#!/usr/bin/env python3


from nose.tools import assert_equal
from ..parity import parity


def test_parity0():
    word = 0b1011
    obs = parity(word)
    exp = 1
    assert_equal(obs, exp)


def test_parity1():
    word = 0b10001000
    obs = parity(word)
    exp = 0
    assert_equal(obs, exp)
