#!/usr/bin/env python3


from nose.tools import assert_equal

from ..two_sorted_arrays_merge import merge_two_sorted_arrays


def test_merge_two_sorted_arrays0() -> None:
    A = [3, 13, 17, None, None, None, None]
    B = [3, 7, 11, 19]
    merge_two_sorted_arrays(A, 3, B, 4)
    exp = [3, 3, 7, 11, 13, 17, 19]
    assert_equal(A, exp)
