#!/bin/python3
# https://leetcode.com/problems/separate-black-and-white-balls/description

# 101 -> 011
# 100 -> 010 -> 001
# 1010 -> 0110 -> 0101 -> 0011


class Solution:
    def minimumSteps(self, str: str) -> int:
        WHITE, BLACK = "0", "1"

        s = [c for c in str]
        left = 0
        right = len(s) - 1

        result = 0
        while left < right:
            if s[left] == WHITE:
                left += 1
            elif s[right] == BLACK:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                result += right - left

        return result


if __name__ == "__main__":

    def test(expected: int, s: str):
        solution = Solution()
        result = solution.minimumSteps(s)
        assert result == expected, f"{result=}, {expected=}, {s=}"

    test(1, "101")
    test(2, "100")
    test(0, "0001")
