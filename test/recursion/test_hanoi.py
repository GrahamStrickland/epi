#!/usr/bin/env python3


from nose.tools import assert_equal

from .hanoi import compute_tower_of_hanoi


def test_compute_tower_of_hanoi() -> None:
    num_rings = 2
    obs = compute_tower_of_hanoi(num_rings)
    exp = [[0, 2], [0, 1], [2, 1]]
    assert_equal(obs, exp)


def test_compute_tower_of_hanoi1() -> None:
    num_rings = 3
    obs = compute_tower_of_hanoi(num_rings)
    exp = [[0, 1], [0, 2], [1, 2], [0, 1], [2, 0], [2, 1], [0, 1]]
    assert_equal(obs, exp)
