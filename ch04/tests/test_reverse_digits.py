#! /usr/bin/env python3


from nose.tools import assert_equal
from ..reverse_digits import reverse_digits


def test_reverse_digits0() -> None:
    x = 42
    obs = reverse_digits(x)
    exp = 24
    assert_equal(obs, exp)


def test_reverse_digits1() -> None:
    x = 158
    obs = reverse_digits(x)
    exp = 851
    assert_equal(obs, exp)


def test_reverse_digits2() -> None:
    x = 0
    obs = reverse_digits(x)
    exp = 0
    assert_equal(obs, exp)


def test_reverse_digits3() -> None:
    x = -12
    obs = reverse_digits(x)
    exp = -21
    assert_equal(obs, exp)


def test_reverse_digits4() -> None:
    x = -1
    obs = reverse_digits(x)
    exp = -1
    assert_equal(obs, exp)