#!/bin/python3
# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

    def isPowerOfTwo_count(self, n: int) -> bool:
        if n == 0:
            return False
        for i in range(0, 32):
            if n & (1 << i) == n:
                return True

        return False