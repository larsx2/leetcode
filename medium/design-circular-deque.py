#!/usr/bin/env python3
# Problem: https://leetcode.com/problems/design-circular-deque/
# Solution: https://leetcode.com/problems/design-circular-deque/submissions/1022454290/


class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class MyCircularDeque:
    def __init__(self, k: int):
        self.limit = k
        self.size = 0
        self.front = self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.size + 1 > self.limit:
            return False

        node = Node(value)
        if self.front is None:
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front = node

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size + 1 > self.limit:
            return False

        node = Node(value)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.front is None:
            return False

        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.rear is None:
            return False

        current, prev = self.front, None
        while current.next:
            prev = current
            current = current.next

        if prev and current:
            self.rear = prev
            self.rear.next = None
        else:
            self.front = self.rear = None

        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.front.val if self.rear else -1

    def getRear(self) -> int:
        return self.rear.val if self.rear else -1

    def isEmpty(self) -> bool:
        return self.front is None

    def isFull(self) -> bool:
        return self.size == self.limit
