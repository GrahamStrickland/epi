#!/usr/bin/env python3


from nose.tools import assert_equal
from typing import List
from ..dutch_national_flag_three_values import dutch_flag_three_values


def test_dutch_flag_():
    A = [0,1,2,0,2,1,1]
    dutch_flag_three_values(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_three_values2():
    A = [0,1,2,0,2,1,1]
    dutch_flag_three_values(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_three_values3():
    A = [0,0,0,0,2,2,2,2,1,1,1,1]
    dutch_flag_three_values(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_three_values4():
    A = [1,0,2,1,0,2,1,0,2]
    dutch_flag_three_values(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_three_values5():
    A = [1,1,1,2,0,0,0,2]
    dutch_flag_three_values(A)
    assert_equal(is_partitioned(A), True)


def is_partitioned(A: List[int]) -> bool:
    j = 0
    for i in range(3):
        val = A[j] 
        while j < len(A) and A[j] == val:
            j += 1
    
    return j == len(A)