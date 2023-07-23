#!/usr/bin/env python3
# https://leetcode.com/problems/asteroid-collision/
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            current = asteroids[i]
            if not stack or current > 0:
                stack.append(current)
                continue

            while stack and stack[-1] > 0 and abs(current) > stack[-1]:
                stack.pop()

            if stack and stack[-1] + current == 0:
                stack.pop()
                continue

            if not stack or stack[-1] < 0:
                stack.append(current)

        return stack
