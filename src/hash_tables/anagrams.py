#!/usr/bin/env python3


import collections
from typing import List, DefaultDict


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    sorted_string_to_anagrams: DefaultDict[
            str, List[str]] = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
        group for group in sorted_string_to_anagrams.values()
        if len(group) >= 2
    ]
