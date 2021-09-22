#!/bin/python3
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        x = 0
        y = 1

        for _ in range(2, n + 1):
            temp = x
            x = y
            y = temp + y

        return y

Solution().fib(4)