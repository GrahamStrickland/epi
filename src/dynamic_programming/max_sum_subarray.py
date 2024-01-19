#!/usr/bin/env python3


from typing import List


def find_maximum_subarray(A: List[int]) -> int:
    max_seen = max_end = 0
    for a in A:
        max_end = max(a, a + max_end)
        max_seen = max(max_seen, max_end)
    return max_seen
