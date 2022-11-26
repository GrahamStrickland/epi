#!/usr/bin/env python3

from nose.tools import assert_equal
from ..enumerate_integers_spiral_order import enumerate_integers_spiral_order


def test_enumerate_integers_spiral_order() -> None:
    n: int = 10
    obs = enumerate_integers_spiral_order(n)
    exp = [(0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (0, 1), (1, 1), (2, 1)]
    assert_equal(obs, exp)
