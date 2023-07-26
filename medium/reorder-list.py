#!/usr/bin/env python3
# https://leetcode.com/problems/reorder-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head

        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        slow = self.reverseList(slow)
        lo, hi = head, slow

        while lo:
            new_hi = hi.next
            new_lo = lo.next
            lo.next = hi
            if new_lo is None:
                hi.next = new_hi
            else:
                hi.next = new_lo

            lo = new_lo
            hi = new_hi
