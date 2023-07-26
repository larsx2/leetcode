#!/usr/bin/env python3
# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        slow = fast = head
        prev = None
        count = 0
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            count += 2
        prev.next = None

        if count % 2 != 0:
            slow = slow.next

        current, prev = slow, None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        slow = prev

        lo, hi = head, slow
        while lo or hi:
            if lo is None or hi is None:
                return False

            if lo.val != hi.val:
                return False

            lo, hi = lo.next, hi.next

        return True
