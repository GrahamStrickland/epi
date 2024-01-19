#!usr/bin/env python3


from is_tree_balanced import is_balanced_binary_tree
from binary_tree import BinaryTreeNode


def test_is_balanced_binary_tree0():
    # Create binary tree.
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

    # Test function.
    obs = is_balanced_binary_tree(A)
    exp = False
    return True if obs == exp else False


def test_is_balanced_binary_tree1():
    # Create binary tree.
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

    # Test function
    obs = is_balanced_binary_tree(A)
    exp = True
    return True if obs == exp else False


print(test_is_balanced_binary_tree0())
print(test_is_balanced_binary_tree1())
