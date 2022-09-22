#!/usr/bin/env python3


from nose.tools import assert_equal
from typing import List
from ..dutch_national_flag_bool_values import dutch_flag_bool


def test_dutch_flag_bool():
    A = [True, False, True, False, True]
    dutch_flag_bool(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_bool2():
    A = [True, True, True, True]
    dutch_flag_bool(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_bool3():
    A = [False, False, False, False]
    dutch_flag_bool(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_bool4():
    A = [True, False, False, False, False]
    dutch_flag_bool(A)
    assert_equal(is_partitioned(A), True)


def test_dutch_flag_bool5():
    A = [True, True, True, True, False]
    dutch_flag_bool(A)
    assert_equal(is_partitioned(A), True)


def is_partitioned(A: List[int]) -> bool:
    first_section = True
    for key in A:
        if first_section and key:
            first_section = False
        if not first_section and not key:
            return False
    return True