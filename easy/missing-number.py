#!/usr/bin/env python
# https://leetcode.com/problems/missing-number

def solve(nums):
    return sum(range(len(nums) + 1))  - sum(nums)


assert solve([3, 0, 1]) == 2
assert solve([0, 1]) == 2
assert solve([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
