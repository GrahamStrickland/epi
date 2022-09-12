#! /usr/bin/env python3


from typing import List


def dutch_flag_three_values(A: List[int]) -> None:
    i = 1
    first, last = 0, len(A) - 1
    val1, val2, val3 = A[first], float('inf'), float('inf')
    while i < last:
        if A[i] == val1:
            A[i], A[first + 1] = A[first + 1], A[i]
            first += 1
            i += 1
        else:
            if val3 == float('inf'):
                val3 = A[i]
                A[i], A[last] = A[last], A[i]
            elif val2 == float('inf'):
                val2 = A[i]
            if A[i] == val3:
                A[i], A[last - 1] = A[last - 1], A[i]
                last -= 1
            else:
                i += 1