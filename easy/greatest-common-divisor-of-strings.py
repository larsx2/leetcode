#!/usr/bin/env python3
# https://leetcode.com/problems/greatest-common-divisor-of-strings/


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s, t = str1, str2
        S, T = len(s), len(t)

        r = list(t)
        while S % len(r) != 0 or T % len(r) != 0:
            r.pop()

        for i in range(max(S, T)):
            idx = i % len(r)

            if i < S and r[idx] != s[i]:
                return ""

            if i < T and r[idx] != t[i]:
                return ""

        return "".join(r)
