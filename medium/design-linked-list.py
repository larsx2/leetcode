#!/usr/bin/env python3
# Problem: https://leetcode.com/problems/design-linked-list/
# Solution: https://leetcode.com/problems/design-linked-list/submissions/1017317841/


class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def get(self, index: int) -> int:
        current = self.head
        while current and index > 0:
            current = current.next
            index -= 1

        if current and index == 0:
            return current.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = LinkedNode(val)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node

    def addAtTail(self, val: int) -> None:
        node = LinkedNode(val)
        if self.tail:
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.head = self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        if self.head is None and index == 0:
            self.addAtTail(val)
            return

        current, pos, prev = self.head, 0, None
        while current:
            if index == pos:
                if prev is None:
                    self.addAtHead(val)
                else:
                    prev.next = LinkedNode(val)
                    prev.next.next = current
                break
            else:
                prev, current, pos = current, current.next, pos + 1

        if current is None and pos == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        current, pos, prev = self.head, 0, None
        while current:
            if index == pos:
                if prev is None:  # index 0
                    self.head = current.next
                    if self.head is None:
                        self.tail = self.head
                else:
                    prev.next = current.next
                    if prev.next is None:
                        self.tail = prev
                break
            else:
                prev, current, pos = current, current.next, pos + 1
