#!/usr/bin/env python3
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)
    current = root
    prev = root
    while current:
        prev = current
        if current.val < val:
            current = current.right
        else:
            current = current.left
    if prev.val > val:
        prev.left = TreeNode(val)
    else:
        prev.right = TreeNode(val)
    return root
