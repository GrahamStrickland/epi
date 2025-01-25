#!/usr/bin/env python3


from src.binary_search_trees.bst import BstNode, search_bst


def test_search_in_bst0():
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

    obs = search_bst(A, 23)
    exp = J

    assert obs == exp
