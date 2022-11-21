#! /usr/bin/env python3


def dutch_flag_four_values(A: list[int]) -> None:
    pivots = [0, 0, 0, len(A) - 1]  # Indices of pivots.
    vals = [A[pivots[0]]]           # Values of pivots.
    vals += [float('inf')] * 3
    while pivots[2] <= pivots[3]:    
        if A[pivots[2]] == vals[0]:
            A[pivots[2]], A[pivots[0]] = A[pivots[0]], A[pivots[2]]
            pivots[0] += 1
            if pivots[1] < pivots[0]:
                pivots[1] += 1
            if pivots[2] < pivots[0]:
                pivots[2] += 1
        else:   # Find remaining pivot values.
            if A[pivots[2]] not in vals:
                if vals[2] == float('inf'):
                    vals[2] = A[pivots[2]]
                elif vals[3] == float('inf'):
                    vals[3] = A[pivots[2]]
                elif vals[1] == float('inf'):
                    vals[1] = A[pivots[2]]

            # Swap A[pivots[2]] to second, third, or fourth partition.
            if A[pivots[2]] == vals[2]:
                A[pivots[2]], A[pivots[1]] = A[pivots[1]], A[pivots[2]]
                pivots[1] += 1
                pivots[2] += 1
            elif A[pivots[2]] == vals[1]:
                pivots[2] += 1
            elif A[pivots[2]] == vals[3]:
                A[pivots[2]], A[pivots[3]] = A[pivots[3]], A[pivots[2]]
                pivots[3] -= 1
