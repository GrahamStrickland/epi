#! /usr/bin/env python3


def mod_power_two(x: int, a: int) -> int:
    if a % 2 == 0:
        return x ^ (a << 1)
    else:
        return x % a