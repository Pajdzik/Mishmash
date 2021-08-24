#!/bin/python3
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        minus = x < 0
        x = abs(x)

        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10

        while len(digits) > 0:
            x *= 10
            x += digits.pop(0)

        if minus:
            x = -x

        if -2**31 > x or 2**31 - 1 < x:
            return 0

        return x