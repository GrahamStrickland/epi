#!/usr/bin/env python3


def is_palindromic(s: str) -> bool:
    # Note that s[~i] for i in [0, len(s) - 1] is s[-(i + 1)].
    return all(s[i] == s[~i] for i in range(len(s) // 2))
