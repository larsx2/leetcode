#!/usr/bin/env python3
# https://leetcode.com/problems/merge-strings-alternately/


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        W1, W2 = len(word1), len(word2)
        result, Len = [], max(W1, W2)
        for i in range(Len):
            if i < W1:
                result.append(word1[i])
            if i < W2:
                result.append(word2[i])
        return "".join(result)
