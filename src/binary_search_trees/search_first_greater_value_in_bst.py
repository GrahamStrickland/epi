#!/usr/bin/env python3


from typing import Optional
from .bst import BstNode


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:   # Root and all keys in left subtree are <= k, so skip them.
            subtree = subtree.right
    return first_so_far
