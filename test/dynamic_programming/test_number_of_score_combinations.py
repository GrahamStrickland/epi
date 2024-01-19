#!/usr/bin/env python3


from nose.tools import assert_equal
from .number_of_score_combinations import num_combinations_for_final_score


def test_num_combinations_for_final_score() -> None:
    final_score = 12
    individual_play_scores = [2,3,7]
    obs = num_combinations_for_final_score(final_score, individual_play_scores)
    exp = 4
    assert_equal(obs, exp)


def test_num_combinations_for_final_score1() -> None:
    final_score = 9
    individual_play_scores = [2,3,7]
    obs = num_combinations_for_final_score(final_score, individual_play_scores)
    exp = 3
    assert_equal(obs, exp)
