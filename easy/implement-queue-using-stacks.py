#!/usr/bin/env python3
# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s1.append(x)
        while self.s1:
            self.s2.append(self.s1.pop())

    def pop(self) -> int:
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        return -1

    def empty(self) -> bool:
        return not self.s2
