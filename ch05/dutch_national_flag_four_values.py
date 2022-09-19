#! /usr/bin/env python3


from typing import List


def dutch_flag_four_values(A: List[int]) -> None:
    i = 1
    pivots = [0, 1, 1, len(A) - 1]  # Indices of pivots.
    vals = [A[pivots[0]]]           # Values of pivots.
    vals += [float('inf')] * 3
    while pivots[2] < pivots[3] and i < pivots[3]:    
        # Find remaining pivot values.
        if A[i] != vals[0]:
            if vals[3] == float('inf'):
                vals[3] = A[i]
                A[i], A[pivots[3]] = A[pivots[3]], A[i]
            elif vals[2] == float('inf') and A[i] != vals[3]:
                vals[2] = A[i]
            elif vals[1] == float('inf') and A[i] != (vals[3] or vals[2]):
                vals[1] = A[i]
        else:
            A[i], A[pivots[0] + 1] = A[pivots[0] + 1], A[i]
            pivots[0], pivots[1] = pivots[0] + 1, pivots[1] + 1 
            i += 1

        # Swap A[i] to second, third, or fourth partition.
        if A[i] == vals[3]:
            A[i], A[pivots[3] - 1] = A[pivots[3] - 1], A[i]
            pivots[3] -= 1
        elif A[i] == vals[2]:
            A[i], A[pivots[2] + 1] = A[pivots[2] + 1], A[i]
            pivots[2] += 1
        elif A[i] == vals[1]:
            A[i], A[pivots[1]] = A[pivots[1]], A[i]
            pivots[1] += 1
            pivots[2] += 1
