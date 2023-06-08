#!/usr/bin/env python
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


def solve(prices: List[int]) -> int:
    return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))


assert solve([7, 1, 5, 3, 6, 4]) == 7
assert solve([1, 2, 3, 4, 5]) == 4
assert solve([7, 6, 4, 3, 1]) == 0
