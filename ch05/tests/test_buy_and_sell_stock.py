#!/usr/bin/env python3


from nose.tools import assert_equal
from ..buy_and_sell_stock import buy_and_sell_stock_once


def test_buy_and_sell_stock_once0():
    prices = [310,315,275,295,260,270,290,230,255,250]
    obs = buy_and_sell_stock_once(prices)
    exp = 30
    assert_equal(obs, exp)


def test_buy_and_sell_stock_once2():
    prices = [310,310,275,275,260,260,260,230,230,230]
    obs = buy_and_sell_stock_once(prices)
    exp = 0
    assert_equal(obs, exp)


def test_buy_and_sell_stock_once3():
    prices = []
    obs = buy_and_sell_stock_once(prices)
    exp = 0
    assert_equal(obs, exp)
