#!/usr/bin/env python3
# https://leetcode.com/problems/fibonacci-number

def solve(n):
    if n not in solve.MEM:
        solve.MEM[n] = solve(n-1) + solve(n-2)
    return solve.MEM[n]

solve.MEM = {0: 0, 1: 1}

assert solve(0) == 0
assert solve(1) == 1
assert solve(2) == 1
assert solve(3) == 2
assert solve(4) == 3
assert solve(10) == 55
