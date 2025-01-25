#!usr/bin/env python3
from src.binary_trees.binary_tree import BinaryTreeNode
from src.binary_trees.tree_traversal import tree_traversal

E = BinaryTreeNode(data=0)
D = BinaryTreeNode(data=28)
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

tree_traversal(A)
