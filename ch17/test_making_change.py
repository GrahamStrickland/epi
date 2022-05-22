#!/usr/bin/env python3


from nose.tools import assert_equal
from .making_change import change_making


def test_change_making() -> None:
    cents = 5
    obs = change_making(cents)
    exp = 1
    assert_equal(obs, exp)


def test_change_making1() -> None:
    cents = 23
    obs = change_making(cents)
    exp = 5
    assert_equal(obs, exp)


def test_change_making2() -> None:
    cents = 76
    obs = change_making(cents)
    exp = 3
    assert_equal(obs, exp)


def test_change_making3() -> None:
    cents = 99
    obs = change_making(cents)
    exp = 8
    assert_equal(obs, exp)
