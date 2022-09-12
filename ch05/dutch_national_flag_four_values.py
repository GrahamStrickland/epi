#! /usr/bin/env python3


from typing import List


def dutch_flag_four_values(A: List[int]) -> None:
    i = 1
    first, mid, last = 0, 1, len(A) - 1
    vals = [ A[first] ]
    vals += [float('inf')] * 3
    while i < mid:
        if A[i] == vals[0]:
            A[i], A[first + 1] = A[first + 1], A[i]
            first += 1
            mid += 1
            i += 1
        else:
            if vals[3] == float('inf'):
                vals[3] = A[i]
                A[i], A[last] = A[last], A[i]
            elif vals[1] == float('inf'):
                vals[1] = A[i]
            elif vals[2] == float('inf'):
                vals[2] = A[i]
            if A[i] == vals[3]:
                A[i], A[last - 1] = A[last - 1], A[i]
                last -= 1
            else:
                if A[i] == vals[1]:
                    mid += 1
                else:
                    A[i], A[mid + 1] = A[mid + 1], A[i]
                i += 1
