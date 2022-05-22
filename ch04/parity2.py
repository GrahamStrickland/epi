#!/usr/bin/env python3


def parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result
