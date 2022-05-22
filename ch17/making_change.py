#!/usr/bin/env python3


def change_making(cents: int) -> int:
    coins = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in coins:
        num_coins += cents // coin
        cents %= coin
    return num_coins
