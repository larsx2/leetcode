#!/usr/bin/env python3
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import operator
from typing import List
from collections import deque


def solve(tokens: List[str]) -> int:
    op = {
        "+": operator.add,
        "-": operator.sub,
        "/": lambda a, b: int(operator.truediv(a, b)),
        "*": operator.mul,
    }
    q = deque()
    for token in tokens:
        if token in op:
            params = reversed([q.pop(), q.pop()])
            value = op[token](*params)
        else:
            value = int(token)
        q.append(value)
    return q.pop()
