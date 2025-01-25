#!usr/bin/env python3
from .binary_tree import BinaryTreeNode


def tree_traversal(root: BinaryTreeNode) -> None:
    if root:
        # Preorder: Processes the root before the traversals of left and right
        # children.
        print("Preorder: %d" % root.data)
        tree_traversal(root.left)
        # Inorder: Processes the root after the traversal of left child and
        # before the traversal of right child.
        print("Inorder: %d" % root.data)
        tree_traversal(root.right)
        # Postorder: Processes the root after the traversals of left and right
        # children.
        print("Postorder: %d" % root.data)
