#!/usr/bin/env python3


from linked_list import *
from is_list_cyclic import has_cycle


def test_has_cycle0() -> None:
    # Create list and enter data.
    list_data = [11,7,5,3,2,4,8,9]
    L = ListNode(data=0, next=None)
    list_iter = ListNode(data=list_data[0], next=None)
    list_data = list_data[1:]
    trail_iter = ListNode(data=0, next=list_iter)
    insert_after(L, list_iter)
    while list_data:
        trail_iter = list_iter
        list_iter = ListNode(list_data[0], next=None)
        list_data = list_data[1:]
        insert_after(trail_iter, list_iter)

    # Check if list has cycle.
    if has_cycle(L):
        print("First node of cycle: {}".format(has_cycle(L)))
    else:
        print("List has no cycle.")


def test_has_cycle1() -> None:
    # Create list and enter data.
    list_data = [11,7,5,3,2,4,8,9]
    L = ListNode(data=0, next=None)
    list_iter = ListNode(data=list_data[0], next=None)
    list_data = list_data[1:]
    trail_iter = ListNode(data=0, next=list_iter)
    insert_after(L, list_iter)
    while list_data:
        trail_iter = list_iter
        list_iter = ListNode(list_data[0], next=None)
        list_data = list_data[1:]
        insert_after(trail_iter, list_iter)

    list_iter = L
    while list_iter.data != 5:
        trail_iter = list_iter
        list_iter = list_iter.next
    trail_iter = list_iter

    while list_iter.data != 8:
        list_iter = list_iter.next

    list_iter.next = trail_iter

    # Check if list has cycle.
    if has_cycle(L):
        print("First node of cycle: {}".format(has_cycle(L).data))
    else:
        print("List has no cycle.")


test_has_cycle0()
test_has_cycle1()
