#! /usr/bin/env python3


from typing import List


def generate_spiral_order(d: int) -> List[List[int]]:
    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_arr = [[0 for i in range(d)] for i in range(d)]

    for i in range(1, d**2 + 1):
        spiral_arr[x][y] = i
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        if (next_x not in range(d)
                or next_y not in range(d)
                or spiral_arr[next_x][next_y] != 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        x, y = next_x, next_y
    return spiral_arr