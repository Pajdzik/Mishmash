#!/bin/python3
# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        mask = 2**32 - 1
        while (num & mask) == num:
            mask >>= 1

        mask = (mask << 1) + 1
        return (mask ^ num)

result = Solution().findComplement(5)
print(result)