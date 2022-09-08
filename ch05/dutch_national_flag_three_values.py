#! /usr/bin/env python3


from typing import List


def dutch_flag_three_values(A: List[int]) -> None:
    i = 1
    first, last = 0, len(A) - 1
    while i < len(A) - 1:
        if A[i] == A[first]:
            A[i], A[first + 1] = A[first + 1], A[i]
            first += 1
        elif A[i] == A[last]:
            A[i], A[last - 1] = A[last - 1], A[i]
            last -= 1
        i += 1