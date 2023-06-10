#!/usr/bin/env python
# https://leetcode.com/problems/first-missing-positive

# time O(n) + space O(n)
def solve_2(nums):
    s, i = set(nums), 1
    while i in s:
        i += 1
    return i


assert solve_2([1, 2, 0]) == 3
assert solve_2([3, 4, -1, 1]) == 2
assert solve_2([7, 8, 9, 11, 12]) == 1
