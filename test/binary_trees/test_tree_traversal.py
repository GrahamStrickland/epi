#!usr/bin/env python3


from binary_tree import BinaryTreeNode
from tree_traversal import tree_traversal


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

tree_traversal(A)
