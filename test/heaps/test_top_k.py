#!/usr/bin/env python3


from nose.tools import assert_equal

from ..top_k import top_k


def test_top_k0():
    k = 6
    stream = "The fat cat sat on the mat.".split(" ")
    it = iter(stream)
    obs = top_k(k, it)
    exp = ["The", "cat", "fat", "sat", "the", "mat."]
    assert_equal(obs, exp)


def test_top_k1():
    k = 3
    stream = "I ate some bulgur wheat.".split(" ")
    it = iter(stream)
    obs = top_k(k, it)
    exp = ["some", "bulgur", "wheat."]
    assert_equal(obs, exp)
