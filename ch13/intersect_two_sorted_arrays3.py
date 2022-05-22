#!/usr/bin/env python3


from typing import List


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:   # A[i] < B[j]
            j += 1
    return intersection_A_B
