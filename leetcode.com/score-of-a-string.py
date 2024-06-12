#!/bin/python3
# https://leetcode.com/problems/score-of-a-string


class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i in range(0, len(s) - 1):
            result += abs(ord(s[i]) - ord(s[i + 1]))

        return result


if __name__ == "__main__":

    def test(expected: int, s: str):
        solution = Solution()
        result = solution.scoreOfString(s)
        assert result == expected, f"expected {expected} but got {result}"

    test(13, "hello")
