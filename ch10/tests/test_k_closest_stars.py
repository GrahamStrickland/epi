#!/usr/bin/env python3


from nose.tools import assert_equal
from typing import List
from ..k_closest_stars import *


def test_find_k_closest_stars() -> None:
    galaxy = [Star(0,1,1), Star(2,2,2), Star(1,3,4),
            Star(2,5,7), Star(8,9,10)]
    stars = iter(galaxy)
    k = 3
    obs = find_k_closest_stars(stars, k)
    exp = [Star(0,1,1), Star(2,2,2), Star(1,3,4)]
    assert_equal(obs, exp)
