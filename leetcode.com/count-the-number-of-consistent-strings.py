#!/bin/python3
# https://leetcode.com/problems/count-the-number-of-consistent-strings

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed_set = set(allowed)

        for word in words:
            chars = set(word)
            if chars.issubset(allowed_set):
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2
    )
    assert (
        solution.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"])
        == 7
    )
    assert (
        solution.countConsistentStrings(
            "cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
        )
        == 4
    )
