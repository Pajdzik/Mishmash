#!/bin/python3
# https://leetcode.com/problems/arranging-coins/

from math import floor, sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return floor(sqrt(2*n + 0.25) - 0.5)

    def arrangeCoins_iterative(self, n: int) -> int:
        i = floor(sqrt(n))

        while n >= ((i + 1) * i) // 2:
            i += 1

        return i - 1

if __name__ == "__main__":
    assert(Solution().arrangeCoins(5) == 2)