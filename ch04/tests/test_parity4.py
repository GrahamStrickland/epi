#!/usr/bin/env python3


from nose.tools import assert_equal
from ..parity4 import parity


def test_parity4_0():
    x = 2**63 - 1
    obs = parity(x)
    exp = 1
    assert_equal(obs, exp)


def test_parity4_1():
    x = 2**63 - 2
    obs = parity(x)
    exp = 0
    assert_equal(obs, exp)
