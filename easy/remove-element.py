#!/usr/bin/env python3
# https://leetcode.com/problems/remove-element


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q = deque()
        for v in nums:
            if val != v:
                q.append(v)
        k = len(q)
        for i in range(k):
            nums[i] = q.popleft()
        return k
