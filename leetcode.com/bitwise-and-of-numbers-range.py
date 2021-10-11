#!/bin/python3
# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift_count = 0

        while left != right:
            left = left >> 1
            right = right >> 1
            shift_count += 1

        return left << shift_count

if __name__ == "__main__":
    Solution().rangeBitwiseAnd(5, 7)