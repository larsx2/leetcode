#!/usr/bin/env python3
# https://leetcode.com/problems/add-strings/


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        N1, N2 = len(num1), len(num2)
        N = max(N1, N2)
        num1 = num1.zfill(N)
        num2 = num2.zfill(N)

        result, carry = [], 0
        for i in range(N - 1, -1, -1):
            val = int(num1[i]) + int(num2[i]) + carry
            carry, digit = divmod(val, 10)
            result.append(str(digit))
        if carry > 0:
            result.append(str(carry))
        return "".join(result)[::-1]
