# https://leetcode.com/problems/add-two-numbers/
import unittest


def make_node_list(li):
    if not li:
        raise ValueError('list must be non-empty')
    head = node = Node(li.pop(0))
    for n in li:
        node.next = Node(n)
        node = node.next
    return head


def deflate_node_list(head):
    li = []
    node = head
    while node:
        li.append(node.val)
        node = node.next
    return li


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(l1, l2):
    left, right, carry = l1, l2, 0
    result = []
    while left or right or carry:
        val = carry
        if left:
            val += left.val
            left = left.next
        if right:
            val += right.val
            right = right.next

        carry, rem = divmod(val, 10)
        result.append(rem)

    return make_node_list(result)


class TestAddTwoNumbers(unittest.TestCase):
    def test_make_node_list(self):
        target = [1, 2, 3]
        head = make_node_list(target)
        node = head
        compare = []
        while node:
            compare.append(node.val)
            node = node.next
        self.assertEqual([1, 2, 3], compare)

    def test_example_1(self):
        l1 = make_node_list([2, 4, 3])
        l2 = make_node_list([5, 6, 4])
        target = [7, 0, 8]
        result = solve(l1, l2)
        self.assertEqual(target, deflate_node_list(result))

    def test_example_2(self):
        l1 = make_node_list([0])
        l2 = make_node_list([0])
        target = [0]
        result = solve(l1, l2)
        self.assertEqual(target, deflate_node_list(result))

    def test_example_3(self):
        l1 = make_node_list([9, 9, 9, 9, 9, 9, 9])
        l2 = make_node_list([9, 9, 9, 9])
        target = [8, 9, 9, 9, 0, 0, 0, 1]
        result = solve(l1, l2)
        self.assertEqual(target, deflate_node_list(result))


if __name__ == '__main__':
    unittest.main()
