#!/usr/bin/env python3
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
