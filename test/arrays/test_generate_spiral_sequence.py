#! /usr/bin/env python3


from ..generate_spiral_sequence import generate_spiral_order_from_sequence


def test_generate_spiral_order() -> None:
    P = list(range(1, 10))
    exp = [[1, 2, 3],
           [8, 9, 4],
           [7, 6, 5]]
    obs = generate_spiral_order_from_sequence(P)
    assert exp == obs


def test_generate_spiral_order2() -> None:
    P = [2**i for i in range(9)]
    exp = [[1, 2, 4],
           [128, 256, 8],
           [64, 32, 16]]
    obs = generate_spiral_order_from_sequence(P)
    assert exp == obs
