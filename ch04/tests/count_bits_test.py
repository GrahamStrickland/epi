from nose.tools import assert_equal
from ..count_bits import count_bits

def test_count_bits_0():
    num = 0
    exp = 0
    obs = count_bits(num)
    assert_equal(exp, obs)

def test_count_bits_15():
    num = 15
    exp = 4
    obs = count_bits(num)
    assert_equal(exp, obs)

def test_count_bits_127():
    num = 127
    exp = 7
    obs = count_bits(num)
    assert_equal(exp, obs)
