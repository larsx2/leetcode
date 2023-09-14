#!/usr/bin/env python3
# Problem: https://leetcode.com/problems/container-with-most-water/
# Solution: https://leetcode.com/problems/container-with-most-water/submissions/1048998311/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, most_water = 0, len(height) - 1, 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            most_water = max(most_water, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most_water
