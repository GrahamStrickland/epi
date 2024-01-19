#!usr/bin/env python3


__all__ = ['BinaryTreeNode']


class BinaryTreeNode:
    def __init__(self, parent=None, data=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

