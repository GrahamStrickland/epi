#!/usr/bin/env python3


import collections
from typing import OrderedDict


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._isbn_price_table: collections.OrderedDict[
                int, int] = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price

    def insert(self, isbn: int, price: int) -> None:
        # We add the value for key only if key is not present - we don't update
        # existing values.
        if isbn not in self._isbn_price_table:
            price = self._isbn_price_table
        elif len(self._isbn_price_table) == self._capacity:
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price

    def erase(self, isbn: int) -> bool:
        return self._isbn_price_table.pop(isbn, None) is not None
