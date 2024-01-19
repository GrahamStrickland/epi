#!/usr/bin/env python3


from linked_list import *
from reverse_sublist import reverse_sublist


def test_reverse_sublist() -> None:
    # Create list and enter data.
    list_data = [11,7,5,3,2]
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

    # Reverse sublist.
    L = reverse_sublist(L, 2, 4)
    list_iter = L.next

    # Print data.
    print("List after reversion: ", end="")
    while list_iter.next != None:
        print("{} ".format(list_iter.data), end="")
        list_iter = list_iter.next
    print("{}".format(list_iter.data))


test_reverse_sublist()
