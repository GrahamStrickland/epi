#!/usr/bin/env python3


from nose.tools import assert_equal

from ..replace_and_remove import replace_and_remove


def test_replace_and_remove0() -> None:
    s = ["a", "b", "a", "c", "_"]
    size = 4
    obs = replace_and_remove(size, s)
    exp = 5
    assert_equal(obs, exp)
    assert_equal(s, ["d", "d", "d", "d", "c"])
