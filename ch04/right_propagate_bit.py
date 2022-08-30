#! /usr/bin/env python3


def right_propagate_rightmost_bit(x: int) -> int:
    return bin(x | (x ^ (x-1)))