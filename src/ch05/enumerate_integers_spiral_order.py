#!/usr/bin/env python3


def enumerate_integers_spiral_order(n: int) -> list[tuple]:
    shift = ((1, 0), (0, -1), (-1, 0), (0, 1))
    direction = x = y = 0
    spiral_ordering: list = []
    int_pair = (0, 0)

    for _ in range(n):
        spiral_ordering += int_pair

    return spiral_ordering
