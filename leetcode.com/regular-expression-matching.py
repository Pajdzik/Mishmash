#!/bin/python3
# https://leetcode.com/problems/regular-expression-matchin

class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        if len(pattern) == 0:
            return len(string) == 0

        match = string and (pattern[0] == string[0] or pattern[0] == '.')

        if len(pattern) >= 2 and pattern[1] == '*':
            return (match and self.isMatch(string[1:], pattern)) \
                or self.isMatch(string, pattern[2:])
        else:
            return match and self.isMatch(string[1:], pattern[1:])


if __name__ == "__main__":
    def test(expected: bool, s: str, p: str):
        result = Solution().isMatch(s, p)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test(False, "aa", "a")
    test(True, "aa", "a*")
    test(True, "ab", ".*")
    test(True, "aab", "c*a*b")
