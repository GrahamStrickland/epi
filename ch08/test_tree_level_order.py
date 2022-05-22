#!/usr/bin/env python3


from binary_tree import BinaryTreeNode
from tree_level_order import binary_tree_depth_order


def test_binary_tree_depth_order() -> bool:
    E = BinaryTreeNode(0)
    D = BinaryTreeNode(28)
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

    obs = binary_tree_depth_order(A)
    exp = [[314], [6,6], [271,561,2,271], [28,0,3,1,28], [17,401,257], [641]]

    return True if obs == exp else False


print(test_binary_tree_depth_order())
