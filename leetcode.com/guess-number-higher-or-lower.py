#!/bin/python3
# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

def guess(n: int) -> int:
    return 8 - n;

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            middle = left + ((right - left) // 2)
            res = guess(middle)
            if res < 0:
                right = middle - 1
            elif res > 0:
                left = middle + 1
            else:
                return middle

        return left

if __name__ == "__main__":
    Solution().guessNumber(10)