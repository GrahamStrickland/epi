#!/usr/bin/env python3


from nose.tools import assert_equal
from .fibonacci import fibonacci


def test_fibonacci() -> None:
    num = 5
    obs = fibonacci(num)
    exp = 5
    assert_equal(obs, exp)


def test_fibonacci1() -> None:
    num = 6
    obs = fibonacci(num)
    exp = 8
    assert_equal(obs, exp)


def test_fibonacci2() -> None:
    num = 10
    obs = fibonacci(num)
    exp = 55
    assert_equal(obs, exp)
