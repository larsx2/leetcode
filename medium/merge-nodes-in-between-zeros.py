#!/usr/bin/env python3
# Problem: https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Solution: https://leetcode.com/problems/merge-nodes-in-between-zeros/submissions/1006615093/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        cursor, current = head, head.next
        while current:
            if current.val == 0:
                cursor.val = val
                if current.next is None:
                    cursor.next = None
                    break
                cursor = cursor.next
                val = 0
            else:
                val += current.val
            current = current.next
        return head
