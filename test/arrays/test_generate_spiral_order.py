#! /usr/bin/env python3


from src.arrays.generate_spiral_order import generate_spiral_order


def test_generate_spiral_order() -> None:
    d = 3
    exp = [[1, 2, 3],
           [8, 9, 4],
           [7, 6, 5]]
    obs = generate_spiral_order(d)
    assert exp == obs


def test_generate_spiral_order2() -> None:
    d = 4
    exp = [[1, 2, 3, 4],
           [12, 13, 14, 5],
           [11, 16, 15, 6],
           [10, 9, 8, 7]]
    obs = generate_spiral_order(d)
    assert exp == obs


def test_generate_spiral_order3() -> None:
    d = 5
    exp = [[1, 2, 3, 4, 5],
           [16, 17, 18, 19, 6],
           [15, 24, 25, 20, 7],
           [14, 23, 22, 21, 8],
           [13, 12, 11, 10, 9]]
    obs = generate_spiral_order(d)
    assert exp == obs
