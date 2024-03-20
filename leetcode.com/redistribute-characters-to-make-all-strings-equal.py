#!/bin/python3
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal

from collections import Counter


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        letter_counter = Counter()

        for word in words:
            for c in word:
                letter_counter[c] += 1

        for value in letter_counter.values():
            if (value % len(words)) != 0:
                return False

        return True


if __name__ == "__main__":
    def test(expected: bool, words: list[str]):
        result = Solution().makeEqual(words)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test(True, ["abc", "aabc", "bc"])
    test(False, ["ab", "a"])
    test(True, ["a", "a"])
    test(False, ["a", "b"])
