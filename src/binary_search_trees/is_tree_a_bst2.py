#!/usr/bin/env python3
import collections
from ..binary_trees.binary_tree import BinaryTreeNode


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    QueueEntry = collections.namedtuple('QueueEntry',
                                        ('node', 'lower', 'upper'))

    bfs_queue = collections.deque(
        [QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue.extend(
                (QueueEntry(front.node.left, front.lower, front.node.data),
                 QueueEntry(front.node.right, front.node.data, front.upper)))

    return True

