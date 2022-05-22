#!/usr/bin/env python3


from is_tree_a_bst import is_binary_tree_bst
from binary_tree import BinaryTreeNode


def test_is_binary_tree_bst0() -> bool:
    # Construct binary tree.
    P = BinaryTreeNode(53)
    O = BinaryTreeNode(47, None, P)
    N = BinaryTreeNode(41)
    M = BinaryTreeNode(31)
    L = BinaryTreeNode(29, None, M)
    K = BinaryTreeNode(37, L, N)
    J = BinaryTreeNode(23, None, K)
    I = BinaryTreeNode(43, J, O)
    H = BinaryTreeNode(13)
    G = BinaryTreeNode(17, H)
    F = BinaryTreeNode(11, None, G)
    E = BinaryTreeNode(5)
    D = BinaryTreeNode(2)
    C = BinaryTreeNode(3, D, E)
    B = BinaryTreeNode(7, C, F)
    A = BinaryTreeNode(19, B, I)

    # Test for BST condition.
    obs = is_binary_tree_bst(A)
    exp = True
    if obs == exp:
        return True
    else:
        return False


def test_is_binary_tree_bst1() -> bool:
    # Construct binary tree.
    D = BinaryTreeNode(28)
    E = BinaryTreeNode(0)
    C = BinaryTreeNode(271, D, E)
    H = BinaryTreeNode(17)
    G = BinaryTreeNode(3, H)
    F = BinaryTreeNode(561, None, G)
    B = BinaryTreeNode(6, C, F)
    M = BinaryTreeNode(641)
    N = BinaryTreeNode(257)
    L = BinaryTreeNode(401, None, M)
    K = BinaryTreeNode(1, L, N)
    J = BinaryTreeNode(2, None, K)
    P = BinaryTreeNode(28)
    O = BinaryTreeNode(271, None, P)
    I = BinaryTreeNode(6, J, O)
    A = BinaryTreeNode(314, B, I)

    # Test for BST condition.
    obs = is_binary_tree_bst(A)
    exp = False
    if obs == exp:
        return True
    else:
        return False


def test_is_binary_tree_bst2() -> bool:
    # Construct binary tree.
    E = BinaryTreeNode(0)
    F = BinaryTreeNode(561)
    D = BinaryTreeNode(28, E, F)
    G = BinaryTreeNode(3)
    C = BinaryTreeNode(271, D, G)
    I = BinaryTreeNode(6)
    J = BinaryTreeNode(2)
    H = BinaryTreeNode(17, I, J)
    B = BinaryTreeNode(6, C, H)
    M = BinaryTreeNode(641)
    N = BinaryTreeNode(257)
    L = BinaryTreeNode(401, M, N)
    O = BinaryTreeNode(271)
    K = BinaryTreeNode(1, L, O)
    A = BinaryTreeNode(314, B, K)

    # Test for BST condition.
    obs = is_binary_tree_bst(A)
    exp = False
    if obs == exp:
        return True
    else:
        return False


print(test_is_binary_tree_bst0())
print(test_is_binary_tree_bst1())
print(test_is_binary_tree_bst2())
