#!/usr/bin/env python3
# https://leetcode.com/problems/valid-parentheses


def solve(s):
    stack = []
    parens = {"}": "{", "]": "[", ")": "("}
    for c in s:
        if c in parens:
            if not stack or stack.pop() != parens[c]:
                return False
        else:
            stack.append(c)
    return not stack


assert solve("()")
assert solve("()[]{}")
assert not solve("(]")
