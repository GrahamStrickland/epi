#!/usr/bin/env python3


from nose.tools import assert_equal

from ..string_integer_interconversion import int_to_string, string_to_int


def test_string_to_int0():
    s = "-123"
    obs = string_to_int(s)
    exp = -123
    assert_equal(obs, exp)


def test_string_to_int1():
    s = "+123"
    obs = string_to_int(s)
    exp = 123
    assert_equal(obs, exp)


def test_string_to_int2():
    s = "-+123"
    obs = string_to_int(s)
    exp = 0
    assert_equal(obs, exp)


def test_string_to_int3():
    s = "+123abc"
    obs = string_to_int(s)
    exp = 123
    assert_equal(obs, exp)


def test_int_to_string0():
    i = -123
    obs = int_to_string(i)
    exp = "-123"
    assert_equal(obs, exp)


def test_int_to_string1():
    i = 123
    obs = int_to_string(i)
    exp = "123"
    assert_equal(obs, exp)


def test_int_to_string2():
    i = 0
    obs = int_to_string(i)
    exp = "0"
    assert_equal(obs, exp)


def test_int_to_string3():
    i = 1234567890
    obs = int_to_string(i)
    exp = "1234567890"
    assert_equal(obs, exp)
