#!/usr/bin/env python3


import bisect
from typing import List


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    def is_present(k):
        i = bisect.bisect_left(B, k)
        return i < len(B) and B[i] == k

    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and is_present(a)]
