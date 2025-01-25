#!/usr/bin/env python3


from three_sum import has_three_sum


def test_has_three_sum() -> bool:
    A = [11, 2, 5, 7, 3]
    t = 21
    obs = has_three_sum(A, t)
    exp = True
    return True if obs == exp else False


def test_has_three_sum1() -> bool:
    A = [11, 2, 5, 7, 3]
    t = 22
    obs = has_three_sum(A, t)
    exp = False
    return True if obs == exp else False


print(test_has_three_sum())
print(test_has_three_sum1())
