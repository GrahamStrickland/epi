#!/usr/bin/env python3


from nose.tools import assert_equal

from ..nearest_repeated_entries import find_nearest_repetition


def test_find_nearest_repetition0() -> None:
    paragraph = "All work and no play makes for no work no fun and no results".split(
        " "
    )
    obs = find_nearest_repetition(paragraph)
    exp = 2
    assert_equal(obs, exp)
