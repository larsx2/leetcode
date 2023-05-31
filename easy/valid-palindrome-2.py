def solve2(s: str):
    i, S = 0, len(s)
    while i < (S//2):
        if s[i] != s[len(s)-i-1]:
            return False
        i += 1
    return True

def solve(s):
    return s == s[::-1]


assert solve("aba") is True
assert solve("abba") is True
assert solve("abbbcbbba") is True
assert solve("abc") is False
assert solve("abcd") is False
