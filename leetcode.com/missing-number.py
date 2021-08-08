#!/bin/python3
# https://leetcode.com/problems/missing-number/

from functools import reduce

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        m = len(nums) + 1
        map = [ False for _ in range(m) ]

        for num in nums:
            map[num] = True

        for i in range(m):
            if not map[i]:
                return i

        return m

Solution().missingNumber([3,0,1])