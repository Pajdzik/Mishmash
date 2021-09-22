#!/bin/python3
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n

        x = 0
        y = 1
        z = 1

        for _ in range(3, n + 1):
            temp = z
            z = x + y + z
            x = y
            y = temp

        return z

Solution().tribonacci(25)