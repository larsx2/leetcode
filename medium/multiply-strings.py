#!/usr/bin/env python3
# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        N1, N2 = len(num1), len(num2)

        products = [[] for _ in range(N1)]
        for i in range(N1 - 1, -1, -1):
            carry, product_idx = 0, N1 - i - 1
            for j in range(N2 - 1, -1, -1):
                val = int(num1[i]) * int(num2[j]) + carry
                carry, digit = divmod(val, 10)
                products[product_idx].append(str(digit))

            if carry > 0:
                products[product_idx].append(str(carry))

        list_of_products = [int("".join(p)[::-1]) for p in products]

        result, inc = 0, 1
        for p in list_of_products:
            result += p * inc
            inc *= 10
        return str(result)
