#!/usr/bin/env python3
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array


def solve_linear(nums):
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    missing = []
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i + 1)
    return missing


def solve_extra_space(nums):
    s = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in s]


tests = [([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]), ([1, 1], [2])]
for params, result in tests:
    assert solve_linear(params[:]) == result
    assert solve_extra_space(params) == result
