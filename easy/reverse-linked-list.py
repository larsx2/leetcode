#!/usr/bin/env python3
# https://leetcode.com/problems/reverse-linked-list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(head):
    li = []
    current = head
    while current:
       li.append(current.val)
       current = current.next
    return li


def from_list(li):
    head = prev = None
    for val in li:
        node = ListNode(val)
        if head is None:
            head = node
        else:
            prev.next = node
        prev = node
    return head


def solve(head):
    q = []
    current = head
    while current:
        q.append(current.val)
        current = current.next

    rhead = ListNode(q.pop()) if q else None
    current = rhead
    while q:
        current.next = ListNode(q.pop())
        current = current.next
    return rhead


assert to_list(solve(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
assert to_list(solve(from_list([1, 2]))) == [2, 1]
assert to_list(solve(from_list([]))) == []
