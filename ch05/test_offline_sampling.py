#!/usr/bin/env python3


from typing import List
from offline_sampling import random_sampling


def test_random_sampling0() -> List[int]:
    k = 3
    A = [3,7,5,11]
    random_sampling(k, A)
    return A


def test_random_sampling1() -> List[int]:
    k = 2
    A = [2,4,6,8,10,12,14,16]
    random_sampling(k, A)
    return A


def test_random_sampling2() -> List[int]:
    k = 5
    A = [1,2,3,5,7,11,13,17,19,23,29]
    random_sampling(k, A)
    return A


print(test_random_sampling0())
print(test_random_sampling1())
print(test_random_sampling2())
