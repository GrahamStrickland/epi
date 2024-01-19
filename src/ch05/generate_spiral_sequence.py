#! /usr/bin/env python3


from math import sqrt, floor


def generate_spiral_order_from_sequence(P: list[int]) -> list[list[int]]:
    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    dimension = floor(sqrt(len(P)))
    spiral_arr = [[0 for _ in range(dimension)] for _ in range(dimension)]

    for i in P:
        spiral_arr[x][y] = i
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        if (next_x not in range(dimension)
                or next_y not in range(dimension)
                or spiral_arr[next_x][next_y] != 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        x, y = next_x, next_y
    return spiral_arr
