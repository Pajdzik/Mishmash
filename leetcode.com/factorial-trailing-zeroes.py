#!/bin/python3
# https://leetcode.com/problems/factorial-trailing-zeroes

# 5! = 1 * 2 * 3 * 4 * 5 = 120 -> 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 -> 1
# 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5040 -> 1
# 8! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 = 40320 -> 1
# 9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 = 362880 -> 1
# 10! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800 -> 2
# 15! = 10! * 11 * 12 * 13 * 14 * 15 = 1307674368000 -> 3
# 20! -> 4
# 25! -> 6 // 25 = 5*5
# 30! -> 7
# 35! -> 8
# 40! -> 9
# 45! -> 10


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        divider = 5

        while divider <= n:
            result += n // divider
            divider *= 5

        return result
