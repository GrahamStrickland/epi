#!/usr/bin/env python3


from ..dutch_national_flag_three_values import dutch_flag_three_values


def test_dutch_flag_three_values() -> None:
    A = [0, 1, 2, 0, 2, 1, 1]
    dutch_flag_three_values(A)
    assert is_partitioned(A)


def test_dutch_flag_three_values2() -> None:
    A = [0, 1, 2, 0, 2, 1, 1]
    dutch_flag_three_values(A)
    assert is_partitioned(A)


def test_dutch_flag_three_values3() -> None:
    A = [0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]
    dutch_flag_three_values(A)
    assert is_partitioned(A)


def test_dutch_flag_three_values4() -> None:
    A = [1, 0, 2, 1, 0, 2, 1, 0, 2]
    dutch_flag_three_values(A)
    assert is_partitioned(A)


def test_dutch_flag_three_values5() -> None:
    A = [1, 1, 1, 2, 0, 0, 0, 2]
    dutch_flag_three_values(A)
    assert is_partitioned(A)


def is_partitioned(A: list[int]) -> bool:
    j = 0
    for _ in range(3):
        if j >= len(A):
            break
        val = A[j] 
        while j < len(A) and A[j] == val:
            j += 1
    
    return j == len(A)
