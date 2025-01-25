#!usr/bin/env python3


from typing import List

from linked_list import ListNode, insert_after
from print_linked_list_in_reverse import print_linked_list_in_reverse


def linked_list_from_arr(arr: List[int]) -> ListNode:
    # Copy elements of arr into linked list
    head = ListNode(data=0, next=None)
    current = ListNode(data=arr.pop(), next=None)
    trail_current = ListNode(data=0, next=current)
    insert_after(head, current)
    while arr:
        trail_current = current
        current.data = arr.pop()
        trail_current.next = current
        insert_after(trail_current, current)
    return head


def test_print_linked_list_in_reverse() -> None:
    # Create list
    head = linked_list_from_arr([1, 2, 3, 4, 5])
    print_linked_list_in_reverse(head)


test_print_linked_list_in_reverse()
