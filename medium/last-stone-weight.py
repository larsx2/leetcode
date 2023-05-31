#!/usr/bin/env python3
# https://leetcode.com/problems/last-stone-weight
from bisect import bisect_left

def solve(stones):
    stones.sort()
    while stones:
        if len(stones) == 1:
            return stones.pop()
        max1 = stones.pop()
        max2 = stones.pop()
        if max1 > max2:
            val = max1 - max2
        else:
            val = max2 - max1
        stones.insert(bisect_left(stones, val), val)
    return 0


def solve2(stones):
    while stones:
        stones.sort()
        if len(stones) == 1:
            return stones.pop()
        max1 = stones.pop()
        max2 = stones.pop()
        if max1 > max2:
            stones.append(max1 - max2)
        else:
            stones.append(max2 - max1)
    return 0


assert solve([2, 7, 4, 1, 8, 1]) == 1
assert solve([1]) == 1
