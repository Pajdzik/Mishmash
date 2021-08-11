#!/bin/python3
# https://leetcode.com/problems/complement-of-base-10-integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        mask = 2**32 - 1
        while (n & mask) == n:
            mask >>= 1

        mask = (mask << 1) + 1
        return (mask ^ n)