#!usr/bin/env python3


__all__ = ['ListNode', 'insert_after', 'delete_after', 'search_list']


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Insert new_node after node.
def insert_after(node: ListNode, new_node: ListNode) -> None:
    new_node.next = node.next
    node.next = new_node


# Delete the node past this one. Assume node is not a tail.
def delete_after(node: ListNode) -> None:
    node.next = node.next.next


def search_list(L: ListNode, key: int) -> ListNode:
    while L and L.data != key:
        L = L.next
    # If key was not present in the list, L will have become null.
    return L
