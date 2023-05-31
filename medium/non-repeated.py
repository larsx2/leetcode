#!/usr/bin/env python3
def solve(s):
    if len(s) < 1:
        return ""

    max_sub = ""
    buf = []

    for i in range(len(s)):
        if s[i] not in buf:
            buf.append(s[i])
            continue

        if len(buf) > len(max_sub):
            max_sub = ''.join(buf)

        buf = [s[i]]

    if len(buf) > len(max_sub):
        max_sub = ''.join(buf)

    return max_sub

assert solve("abcabcbb") == "abc"
assert solve("bbbbb") == "b"
assert solve("pwwkew") == "wke"
assert solve(" ") == " "
assert solve("au") == "au"
