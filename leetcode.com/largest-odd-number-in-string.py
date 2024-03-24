#!/bin/python3
# https://leetcode.com/problems/largest-odd-number-in-string

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if num[i] in ['1', '3', '5', '7', '9']:
                return num[:i + 1]

        return ""


if __name__ == "__main__":
    def test(expected: str, num: str):
        result = Solution().largestOddNumber(num)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test("5", "52")
    test("", "4206")
    test("35427", "35427")
