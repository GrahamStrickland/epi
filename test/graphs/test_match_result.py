#!/usr/bin/env python3

from src.graphs.match_result import MatchResult, can_team_a_beat_team_b


def test_can_team_a_beat_team_b0():
    matches = [
        MatchResult(winning_team="A", losing_team="B"),
        MatchResult(winning_team="B", losing_team="C"),
        MatchResult(winning_team="C", losing_team="A"),
    ]

    assert can_team_a_beat_team_b(matches, "A", "B")


def test_can_team_a_beat_team_b1():
    matches = [
        MatchResult(winning_team="A", losing_team="B"),
        MatchResult(winning_team="B", losing_team="C"),
        MatchResult(winning_team="A", losing_team="C"),
    ]

    assert can_team_a_beat_team_b(matches, "C", "A")
