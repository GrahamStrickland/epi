#!/usr/bin/env python3


import functools


def ss_decode_col_id(col: str) -> int:
    return functools.reduce(
            lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)
