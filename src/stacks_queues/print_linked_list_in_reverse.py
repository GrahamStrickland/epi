#!usr/bin/env python3


from linked_list import ListNode


def print_linked_list_in_reverse(head: ListNode) -> None:
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())
