#!usr/bin/env python3
import collections

from .binary_tree import BinaryTreeNode


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple(
        "BalancedStatusWithHeight", ("balanced", "height")
    )

    # Frst value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of the tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced
