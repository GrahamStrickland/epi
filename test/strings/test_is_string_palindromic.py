#!/usr/bin/env python3


from nose.tools import assert_equal

from ..is_string_palindromic import is_palindromic


def test_is_palindromic0():
    test_str = "Madam, I'm Adam"
    obs = is_palindromic(test_str)
    exp = False
    assert_equal(obs, exp)


def test_is_palindromic1():
    test_str = "racecar"
    obs = is_palindromic(test_str)
    exp = True
    assert_equal(obs, exp)


def test_is_palindromic2():
    test_str = "Sam I am"
    obs = is_palindromic(test_str)
    exp = False
    assert_equal(obs, exp)
