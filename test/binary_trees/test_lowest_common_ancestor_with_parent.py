#!/usr/bin/env python3


from src.binary_trees.binary_tree import BinaryTreeNode
from src.binary_trees.lowest_common_ancestor_with_parent import lca


# Create binary tree.
M = BinaryTreeNode(None, 641)
N = BinaryTreeNode(None, 257)
L = BinaryTreeNode(None, 401, None, M)
H = BinaryTreeNode(None, 17)
P = BinaryTreeNode(None, 28)
K = BinaryTreeNode(None, 1, L, N)
G = BinaryTreeNode(None, 3, H)
E = BinaryTreeNode(None, 0)
D = BinaryTreeNode(None, 28)
O = BinaryTreeNode(None, 271, None, P)
J = BinaryTreeNode(None, 2, None, K)
F = BinaryTreeNode(None, 561, None, G)
C = BinaryTreeNode(None, 271, D, E)
I = BinaryTreeNode(None, 6, J, O)
B = BinaryTreeNode(None, 6, C, F)
A = BinaryTreeNode(None, 314, B, I)
M.parent = L
N.parent = L.parent = K
H.parent = G
P.parent = O
K.parent = J
G.parent = F
E.parent = D.parent = C
O.parent = J.parent = I
F.parent = C.parent = B
I.parent = B.parent = A


def test_lca0() -> None:
    obs = lca(D, E)
    exp = C
    assert obs == exp


def test_lca1() -> None:
    obs = lca(D, K)
    exp = A
    assert obs == exp


def test_lca2() -> None:
    obs = lca(M, P)
    exp = I
    assert obs == exp

