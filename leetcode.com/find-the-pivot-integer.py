#!/bin/python3
# https://leetcode.com/problems/find-the-pivot-integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_l = l = 1
        sum_r = r = n

        while l != r:
            if sum_l < sum_r:
                l = l + 1
                sum_l = sum_l + l
            else:
                r = r - 1
                sum_r = sum_r + r

        if sum_l == sum_r:
            return l
        else:
            return -1


if __name__ == "__main__":
    def test(expected: int, n: int):
        result = Solution().pivotInteger(n)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test(1, 1)
    test(6, 8)
    test(-1, 4)
