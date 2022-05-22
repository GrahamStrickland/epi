#!/usr/bin/env python3


from nose.tools import assert_equal
from typing import List
from ..dutch_national_flag3 import dutch_flag_partition


def test_dutch_flag_partition0():
    A = [0,1,2,0,2,1,1]
    pivot_index = 3
    pivot = A[pivot_index]
    dutch_flag_partition(pivot_index, A)
    assert_equal(is_partitioned(pivot, A), True)


def test_dutch_flag_partition1():
    A = [0,1,2,0,2,1,1]
    pivot_index = 2
    pivot = A[pivot_index]
    dutch_flag_partition(pivot_index, A)
    assert_equal(is_partitioned(pivot, A), True)


def is_partitioned(pivot: int, A: List[int]) -> bool:
    lesser = True
    greater = False
    for i in A:
        if lesser:
            if i == pivot:
                lesser = False
            elif i > pivot:
                return False
        elif not lesser and not greater:
            if i > pivot:
                greater = True
            elif i < pivot:
                return False
        else:
            if i < pivot or i == pivot:
                return False
    return True
