#!/usr/bin/env python3
# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solution: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1023764325/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if target == numbers[i] + numbers[j]:
                return [i + 1, j + 1]
            if target > numbers[i] + numbers[j]:
                i += 1
            else:
                j -= 1
