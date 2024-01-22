#!usr/bin/env python3
from src.binary_trees.is_tree_balanced import is_balanced_binary_tree
from src.binary_trees.binary_tree import BinaryTreeNode


def test_is_balanced_binary_tree0():
    D = BinaryTreeNode(data=28)
    E = BinaryTreeNode(data=0)
    C = BinaryTreeNode(data=271, left=D, right=E)
    H = BinaryTreeNode(data=17)
    G = BinaryTreeNode(data=3, left=H)
    F = BinaryTreeNode(data=561, right=G)
    B = BinaryTreeNode(data=6, left=C, right=F)
    M = BinaryTreeNode(data=641)
    N = BinaryTreeNode(data=257)
    L = BinaryTreeNode(data=401, right=M)
    K = BinaryTreeNode(data=1, left=L, right=N)
    J = BinaryTreeNode(data=2, right=K)
    P = BinaryTreeNode(data=28)
    O = BinaryTreeNode(data=271, right=P)
    I = BinaryTreeNode(data=6, left=J, right=O)
    A = BinaryTreeNode(data=314, left=B, right=I)

    obs = is_balanced_binary_tree(A)
    exp = False

    assert obs == exp


def test_is_balanced_binary_tree1():
    E = BinaryTreeNode(data=0)
    F = BinaryTreeNode(data=561)
    D = BinaryTreeNode(data=28, left=E, right=F)
    G = BinaryTreeNode(data=3)
    C = BinaryTreeNode(data=271, left=D, right=G)
    I = BinaryTreeNode(data=6)
    J = BinaryTreeNode(data=2)
    H = BinaryTreeNode(data=17, left=I, right=J)
    B = BinaryTreeNode(data=6, left=C, right=H)
    M = BinaryTreeNode(data=641)
    N = BinaryTreeNode(data=257)
    L = BinaryTreeNode(data=401, left=M, right=N)
    O = BinaryTreeNode(data=271)
    K = BinaryTreeNode(data=1, left=L, right=O)
    A = BinaryTreeNode(data=314, left=B, right=K)

    # Test function
    obs = is_balanced_binary_tree(A)
    exp = True

    assert obs == exp

