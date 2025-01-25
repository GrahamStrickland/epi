#!/usr/bin/env python3

from .fibonacci2 import fibonacci


def test_fibonacci() -> None:
    num = 5
    obs = fibonacci(num)
    exp = 5

    assert obs == exp


def test_fibonacci1() -> None:
    num = 6
    obs = fibonacci(num)
    exp = 8

    assert obs == exp


def test_fibonacci2() -> None:
    num = 10
    obs = fibonacci(num)
    exp = 55

    assert obs == exp
