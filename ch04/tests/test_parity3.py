#!/usr/bin/env python3


from nose.tools import assert_equal
from ..parity3 import parity3


def test_parity3_0():
    x = 2**63 - 1
    obs = parity3(x)
    exp = 1
    assert_equal(obs, exp)


def test_parity3_1():
    x = 2**63 - 2
    obs = parity3(x)
    exp = 0
    assert_equal(obs, exp)
