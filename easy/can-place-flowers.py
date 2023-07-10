#!/usr/bin/env python3
# https://leetcode.com/problems/can-place-flowers

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 1 and flowerbed == [0]:
            return True

        prev = 0
        L = len(flowerbed)
        for i in range(1, L):
            if n == 0:
                return True

            if prev == flowerbed[i - 1] == flowerbed[i] == 0:
                flowerbed[i - 1] = 1
                n -= 1

            elif L - 1 == i and flowerbed[i - 1] == flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
            prev = flowerbed[i - 1]

        return n == 0
