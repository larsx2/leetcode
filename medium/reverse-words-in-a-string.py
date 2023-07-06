#!/usr/bin/env python3
# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def quick_solution(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def lstrip(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] != " ":
                return s[i:]
        return s

    def rstrip(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                return s[: i + 1]
        return s

    def reverseWords(self, s: str) -> str:
        s = self.rstrip(self.lstrip(s))
        words = []
        word = []
        for i in range(len(s)):
            if s[i] != " ":
                word.append(s[i])
                continue

            if s[i] == " " and word:
                words.append("".join(word))
                word = []
        if word:
            words.append("".join(word))

        return " ".join(reversed(words))
