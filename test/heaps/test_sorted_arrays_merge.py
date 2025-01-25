#!/usr/bin/env python3


from nose.tools import assert_equal

from ..sorted_arrays_merge import (merge_sorted_arrays,
                                   merge_sorted_arrays_pythonic)


def test_merge_sorted_arrays0():
    sorted_arrays = [[3, 5, 7], [0, 6], [0, 6, 28]]
    obs = merge_sorted_arrays(sorted_arrays)
    exp = [0, 0, 3, 5, 6, 6, 7, 28]
    assert_equal(obs, exp)


def test_merge_sorted_arrays1():
    sorted_arrays = [[1, 2, 3, 4, 5], [0]]
    obs = merge_sorted_arrays(sorted_arrays)
    exp = [0, 1, 2, 3, 4, 5]
    assert_equal(obs, exp)


def test_merge_sorted_arrays2():
    sorted_arrays = [[1, 3, 5, 50], [1, 2, 4], [70, 100]]
    obs = merge_sorted_arrays(sorted_arrays)
    exp = [1, 1, 2, 3, 4, 5, 50, 70, 100]
    assert_equal(obs, exp)


def test_merge_sorted_arrays_pythonic0():
    sorted_arrays = [[3, 5, 7], [0, 6], [0, 6, 28]]
    obs = merge_sorted_arrays_pythonic(sorted_arrays)
    exp = [0, 0, 3, 5, 6, 6, 7, 28]
    assert_equal(obs, exp)


def test_merge_sorted_arrays_pythonic1():
    sorted_arrays = [[1, 2, 3, 4, 5], [0]]
    obs = merge_sorted_arrays_pythonic(sorted_arrays)
    exp = [0, 1, 2, 3, 4, 5]
    assert_equal(obs, exp)


def test_merge_sorted_arrays_pythonic2():
    sorted_arrays = [[1, 3, 5, 50], [1, 2, 4], [70, 100]]
    obs = merge_sorted_arrays_pythonic(sorted_arrays)
    exp = [1, 1, 2, 3, 4, 5, 50, 70, 100]
    assert_equal(obs, exp)
