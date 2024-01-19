#!/usr/bin/env python3


import functools


@functools.lru_cache(None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
