#!/usr/bin/env python3
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [(currCandies + extraCandies) >= maxCandies for currCandies in candies]
