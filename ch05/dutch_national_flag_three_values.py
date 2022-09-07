#! /usr/bin/env python3


from typing import List


def dutch_flag_three_values(A: List[int]) -> None:
    val1, val2, val3 = A[0], float('inf'), float('inf')
    i = j = 0
    while A[i] == val1 and i < len(A):
        if A[i] != val1 and A[i] != val2:
            val2 = A[i]
            j = i
        else:
            i += 1
    while (A[i] == val1 or A[i] == val2) and i < len(A):
        if A[i] == val1:
            A[i], A[j] = A[j], A[i]
            j += 1
            i += 1
        elif A[i] == val2:
            i += 1
        else:
            val3 = A[i]