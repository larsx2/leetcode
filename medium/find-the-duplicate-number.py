#!/usr/bin/env python3
# https://leetcode.com/problems/find-the-duplicate-number


def solve(nums):
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


tests = [([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3)]
for params, result in tests:
    assert solve(params) == result
