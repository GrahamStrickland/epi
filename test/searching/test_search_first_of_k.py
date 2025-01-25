#!/usr/bin/env python3


from nose.tools import assert_equal

from ..search_first_key import search_first_of_k


def test_search_first_of_k0():
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    obs = search_first_of_k(A, 108)
    exp = 3
    assert_equal(obs, exp)


def test_search_first_of_k1():
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    obs = search_first_of_k(A, 285)
    exp = 6
    assert_equal(obs, exp)


def test_search_first_of_k2():
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    obs = search_first_of_k(A, -5)
    exp = -1
    assert_equal(obs, exp)


def test_search_first_of_k3():
    A = []
    obs = search_first_of_k(A, 108)
    exp = -1
    assert_equal(obs, exp)
