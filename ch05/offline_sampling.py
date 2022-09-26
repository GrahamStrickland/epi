#!/usr/bin/env python3


import random
from typing import List

def random_sampling(k: int, A: List[int]) -> None:
    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]


def test_random_sampling() -> List[int]:
    k = 3
    A = [3,7,5,11]
    random_sampling(k, A)
    return A


def test_random_sampling2() -> List[int]:
    k = 2
    A = [2,4,6,8,10,12,14,16]
    random_sampling(k, A)
    return A


def test_random_sampling3() -> List[int]:
    k = 5
    A = [1,2,3,5,7,11,13,17,19,23,29]
    random_sampling(k, A)
    return A


def test_random_sampling4() -> List[int]:
    k = 5
    A = list(range(100))
    random_sampling(k, A)
    return A


print(test_random_sampling())
print(test_random_sampling2())
print(test_random_sampling3())
print(test_random_sampling4())