#! /usr/bin/env python3


def longest_subarray_equal(A: list[int]) -> int:
    i = 0
    longest, current, current_val = 1, 1, A[i]
    i += 1
    while i < len(A):
        if A[i] == current_val:
            current += 1
        else:
            current_val = A[i]
            current = 1
        if longest < current:
            longest = current
        i += 1

    return longest
