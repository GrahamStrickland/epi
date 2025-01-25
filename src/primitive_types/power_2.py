#! /usr/bin/env python3


def power_2(x: int) -> bool:
    return x & (x - 1) == 0
