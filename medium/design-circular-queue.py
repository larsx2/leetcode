#!/usr/bin/env python3
# Problem: https://leetcode.com/problems/design-circular-queue/
# Solution: https://leetcode.com/problems/design-circular-queue/submissions/1021843085/


class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):
        self.limit = k
        self.front = self.rear = None
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size >= self.limit:
            return False

        if self.isEmpty():
            self.front = self.rear = Node(value)
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.front:
            self.front = self.front.next
            self.size -= 1

            if self.front is None:
                self.rear = None
            return True
        return False

    def Front(self) -> int:
        return self.front.val if self.front else -1

    def Rear(self) -> int:
        return self.rear.val if self.rear else -1

    def isEmpty(self) -> bool:
        return self.front is None and self.rear is None

    def isFull(self) -> bool:
        return self.size == self.limit
