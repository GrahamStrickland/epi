#!/usr/bin/env python3


from typing import Optional


__all__ = ['BstNode', 'search_bst']


class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    return (tree if not tree or tree.data == key else search_bst(
        tree.left, key) if key < tree.data else search_bst(tree.right, key))
