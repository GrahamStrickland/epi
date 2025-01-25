#!/usr/bin/env python3


from nose.tools import assert_equal

from ..spreadsheet_encoding import ss_decode_col_id


def test_ss_decode_col_id0() -> None:
    col = "A"
    obs = ss_decode_col_id(col)
    exp = 1
    assert_equal(obs, exp)


def test_ss_decode_col_id1() -> None:
    col = "D"
    obs = ss_decode_col_id(col)
    exp = 4
    assert_equal(obs, exp)


def test_ss_decode_col_id2() -> None:
    col = "AA"
    obs = ss_decode_col_id(col)
    exp = 27
    assert_equal(obs, exp)


def test_ss_decode_col_id3() -> None:
    col = "ZZ"
    obs = ss_decode_col_id(col)
    exp = 702
    assert_equal(obs, exp)
