#!/bin/python3
# https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum = 0

        while n > 0:
            sum += (n % k)
            n //= k

        return sum
