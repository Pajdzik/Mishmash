#!/bin/python3
# https://leetcode.com/problems/is-subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0

        while si < len(s) and ti < len(t):
            while ti < len(t) and s[si] != t[ti]:
                ti += 1

            if ti < len(t) and s[si] == t[ti]:
                si += 1
                ti += 1

        return si == len(s)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isSubsequence("aaaaaa", "bbaaaa") == False
    assert solution.isSubsequence("b", "c") == False
    assert solution.isSubsequence("abc", "ahbgdc") == True
    assert solution.isSubsequence("axc", "ahbgdc") == False
    assert solution.isSubsequence("", "ahbgdc") == True
    assert solution.isSubsequence("abc", "") == False
    assert solution.isSubsequence("abc", "abc") == True
