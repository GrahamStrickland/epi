#!/usr/bin/env python3


from nose.tools import assert_equal

from ..is_anonymous_letter_constructible import (
    is_letter_constructible_from_magazine,
    is_letter_constructible_from_magazine_pythonic)


def test_is_letter_constructible_from_magazine0():
    letter_text = "Hello, my name is Gordon."
    magazine_text = "Hello, my name is Gordon. What's your name?"
    obs = is_letter_constructible_from_magazine(letter_text, magazine_text)
    exp = True
    assert_equal(obs, exp)


def test_is_letter_constructible_from_magazine1():
    letter_text = ""
    magazine_text = "Hello, world!"
    obs = is_letter_constructible_from_magazine(letter_text, magazine_text)
    exp = True
    assert_equal(obs, exp)


def test_is_letter_constructible_from_magazine2():
    letter_text = "Hello, my name is Gordon. What is your name?"
    magazine_text = "Hello, my name is Gordon and I have a dog"
    obs = is_letter_constructible_from_magazine(letter_text, magazine_text)
    exp = False
    assert_equal(obs, exp)


def test_is_letter_constructible_from_magazine_pythonic0():
    letter_text = "Hello, my name is Gordon."
    magazine_text = "Hello, my name is Gordon. What's your name?"
    obs = is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text)
    exp = True
    assert_equal(obs, exp)


def test_is_letter_constructible_from_magazine_pythonic1():
    letter_text = ""
    magazine_text = "Hello, world!"
    obs = is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text)
    exp = True
    assert_equal(obs, exp)


def test_is_letter_constructible_from_magazine_pythonic2():
    letter_text = "Hello, my name is Gordon. What is your name?"
    magazine_text = "Hello, my name is Gordon and I have a dog"
    obs = is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text)
    exp = False
    assert_equal(obs, exp)
