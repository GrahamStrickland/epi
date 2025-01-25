#!/usr/bin/env python3


def buy_and_sell_stock_once(prices: list[float]) -> float:
    min_price_so_far, max_profit = float("inf"), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit
