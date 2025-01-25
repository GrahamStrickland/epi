#!/usr/bin/env python3


from lru_cache import LRUCache


def main() -> None:
    cache = LRUCache(10)

    cache.insert(1234567890, 19.99)

    cache.lookup(1234567890)

    cache.erase(1234567890)

    cache.lookup(1234567890)


main()
