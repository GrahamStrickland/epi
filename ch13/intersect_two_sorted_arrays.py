#!/usr/bin/env python3


from typing import List


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and a in B]
