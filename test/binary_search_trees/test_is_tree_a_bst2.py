#!/usr/bin/env python3
from src.binary_search_trees.is_tree_a_bst2 import is_binary_tree_bst
from src.binary_trees.binary_tree import BinaryTreeNode


def test_is_binary_tree_bst0() -> bool:
    # Construct binary tree.
    P = BinaryTreeNode(data=53)
    O = BinaryTreeNode(data=47, right=P)
    N = BinaryTreeNode(data=41)
    M = BinaryTreeNode(data=31)
    L = BinaryTreeNode(data=29, right=M)
    K = BinaryTreeNode(data=37, left=L, right=N)
    J = BinaryTreeNode(data=23, right=K)
    I = BinaryTreeNode(data=43, left=J, right=O)
    H = BinaryTreeNode(data=13)
    G = BinaryTreeNode(data=17, left=H)
    F = BinaryTreeNode(data=11, right=G)
    E = BinaryTreeNode(data=5)
    D = BinaryTreeNode(data=2)
    C = BinaryTreeNode(data=3, left=D, right=E)
    B = BinaryTreeNode(data=7, left=C, right=F)
    A = BinaryTreeNode(data=19, left=B, right=I)

    # Test for BST condition.
    obs = is_binary_tree_bst(A)
    exp = True
    
    assert obs == exp


def test_is_binary_tree_bst1() -> bool:
    # Construct binary tree.
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

    # Test for BST condition.
    obs = is_binary_tree_bst(A)
    exp = False

    assert obs == exp


def test_is_binary_tree_bst2() -> bool:
    # Construct binary tree.
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

    # Test for BST condition.
    obs = is_binary_tree_bst(A)
    exp = False

    assert obs == exp

