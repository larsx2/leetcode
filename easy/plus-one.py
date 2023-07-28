#!/usr/bin/env python3
# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(d) for d in list(str(int("".join(map(str, digits))) + 1))]
