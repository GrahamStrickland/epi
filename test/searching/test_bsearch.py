#!/usr/bin/env


from nose.tools import assert_equal
from ..bsearch import bsearch


def test_bsearch0():
    A = []
    obs = bsearch(1, A)
    exp = -1
    assert_equal(obs, exp)


def test_bsearch1():
    A = [1,2,3,4,5]
    obs = bsearch(3, A)
    exp = 2
    assert_equal(obs, exp)


def test_bsearch2():
    A = [1,11,33,55,88,101]
    obs = bsearch(102, A)
    exp = -1
    assert_equal(obs, exp)


def test_bsearch3():
    A = [1,11,33,55,88,101]
    obs = bsearch(101, A)
    exp = 5
    assert_equal(obs, exp)
