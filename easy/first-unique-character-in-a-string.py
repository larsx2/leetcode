#!/usr/bin/env python3
# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # from collections import Counter
        # counter = Counter(s)
        counter = dict()
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1
