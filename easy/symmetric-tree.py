#!/usr/bin/env python3
# https://leetcode.com/problems/symmetric-tree/
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> bool:
    q = deque()
    q.append(root.left)
    q.append(root.right)

    while q:
        right, left = q.pop(), q.pop()
        if (not right and left) or (not left and right):
            return False

        if not right and not left:
            return True

        if right.val != left.val:
            return False

        if left.left or right.right:
            q.append(left.left)
            q.append(right.right)

        if left.right or right.left:
            q.append(left.right)
            q.append(right.left)

    return True
