#!/usr/bin/env python3


from typing import List

from two_sum import has_two_sum


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A)
