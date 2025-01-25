#!/usr/bin/env python3


from src.binary_search_trees.bst import BstNode
from src.binary_search_trees.search_first_greater_value_in_bst import \
    find_first_greater_than_k

P = BstNode(53)
O = BstNode(47, None, P)
N = BstNode(41)
M = BstNode(31)
L = BstNode(29, None, M)
K = BstNode(37, L, N)
J = BstNode(23, None, K)
I = BstNode(43, J, O)
H = BstNode(13)
G = BstNode(17, H)
F = BstNode(11, None, G)
E = BstNode(5)
D = BstNode(2)
C = BstNode(3, D, E)
B = BstNode(7, C, F)
A = BstNode(19, B, I)


def test_find_first_greater_than_k0() -> None:
    obs = find_first_greater_than_k(A, 23)
    exp = L
    assert obs == exp
