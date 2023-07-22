#!/usr/bin/env python3
# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursiveInorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
            return result

        return inorder(root)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        stack = []
        current = root
        while True:
            while current:
                stack.append(current)
                current = current.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            current = node.righ
