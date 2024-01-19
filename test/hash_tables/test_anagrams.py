#!/usr/bin/env python3


from nose.tools import assert_equal
from ..anagrams import find_anagrams


def test_find_anagrams():
    dictionary = ["debitcard", "elvis", "silent",
            "badcredit", "lives", "freedom", "listen",
            "levis", "money"]
    obs = find_anagrams(dictionary)
    exp = [["debitcard", "badcredit"], ["elvis", "lives", "levis"], ["silent", "listen"]]
    assert_equal(obs, exp)
