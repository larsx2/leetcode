#!/usr/bin/env python3
# https://leetcode.com/problems/search-in-a-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    current = root
    while current:
        if current.val == val:
            return current
        if val > current.val:
            current = current.right
        else:
            current = current.left
    return None
