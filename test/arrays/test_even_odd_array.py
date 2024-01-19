#!/usr/bin/env python3


from src.arrays.even_odd_array import even_odd


def test_even_odd_array0() -> None:
    arr = [2, 3, 4, 6, 7]
    even_odd(arr)
    assert check_even_odd(arr)


def test_even_odd_array1() -> None:
    arr = [2, 4, 6]
    even_odd(arr)
    assert check_even_odd(arr)


def test_even_odd_array2() -> None:
    arr = [3, 5, 7]
    even_odd(arr)
    assert check_even_odd(arr)


def check_even_odd(A: list[int]) -> bool:
    odd_flag = False
    for i in A:
        if not odd_flag:
            if i % 2 != 0:
                odd_flag = True
        elif i % 2 == 0:
            return False
    return True
