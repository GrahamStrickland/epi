#!/usr/bin/env python3


from nose.tools import assert_equal
from .linked_list import *
from .sorted_lists_merge import merge_two_sorted_lists
from typing import List


def merge_and_compare(L1_arr: List[int], L2_arr: List[int]) -> bool:
    # Copy elements of L1_arr into L1 linked list
    L1 = ListNode(data=0, next=None)
    current = L1
    trail_current = ListNode(data=0, next=current)
    while L1_arr:
        current = ListNode(L1_arr.pop(), next=None)
        trail_current = ListNode(L1.next, next=current)
        insert_after(trail_current, current)


    # Copy elements of L2_arr into L2 linked list
    L2 = ListNode(data=0, next=None)
    current = L2
    trail_current = ListNode(data=0, next=current)
    while L2_arr:
        current = ListNode(L2_arr.pop(), next=None)
        trail_current = ListNode(L2.next, next=current)
        insert_after(trail_current, current)

    # Merge two linked lists
    L3 = merge_two_sorted_lists(L1, L2)

    # Test against sorted array
    L3_arr = sorted(L1_arr + L2_arr)
    current = L3
    i = 0
    while current.data != 0:
        if (L3_arr[i] != current.data):
            return False
        current = current.next
        i += 1
    return True


def test_merge_two_sorted_lists0():
    L1 = [2,5,7]
    L2 = [3,11]
    obs = merge_and_compare(L1,L2)
    exp = True
    assert_equal(obs,exp)


def test_merge_two_sorted_lists1():
    L1 = [2,45,190,2001]
    L2 = [1,2,3,4,5,6,7,8,9,10]
    obs = merge_and_compare(L1,L2)
    exp = True


def test_merge_two_sorted_lists2():
    L1 = [1]
    L2 = [1]
    obs = merge_and_compare(L1,L2)
    exp = True


def test_merge_two_sorted_lists3():
    L1 = [1]
    L2 = [1000, 20000, 4000000]
    obs = merge_and_compare(L1,L2)
    exp = True
