#! /usr/bin/env python3


from typing import List


def dutch_flag_bool(A: List[int]) -> None:
    first = 0
    last = len(A) - 1
    while first <= last:
        if A[first]:
            A[first], A[last] = A[last], A[first]
            last -= 1
        else:
            first += 1
