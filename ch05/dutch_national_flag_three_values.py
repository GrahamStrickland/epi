#! /usr/bin/env python3


from typing import List
import pdb


def dutch_flag_three_values(A: List[int]) -> None:
    i = 1
    first, last = 0, len(A) - 1
    val1, val2, val3 = A[first], float('inf'), float('inf')
    while i < len(A) - 1:
        if A[i] == val1:
            A[i], A[first + 1] = A[first + 1], A[i]
            first += 1
        else:
            if val3 == float('inf'):
                if val3 != A[last]:
                    A[i], A[last] = A[last], A[i]
                    i -= 1
                val3 = A[i]
            elif val2 == float('inf'):
                val2 = A[i]
            elif A[i] == val3:
                A[i], A[last - 1] = A[last - 1], A[i]
                last -= 1
        i += 1


if __name__ == "__main__":
    pdb.set_trace()
    A = [1,0,2,1,0,2,1,0,2]
    dutch_flag_three_values(A)