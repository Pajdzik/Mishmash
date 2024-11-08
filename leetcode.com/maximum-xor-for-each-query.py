#!/bin/python3
# https://leetcode.com/problems/maximum-xor-for-each-query

from typing import List

# 00
# 01
# 01
# 11
# xor
# 11


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result = []
        max_bits = 2**maximumBit - 1

        all_xor = 0
        for num in nums:
            all_xor ^= num

        for i in range(len(nums) - 1, -1, -1):
            res = max_bits - all_xor
            result.append(res)
            all_xor ^= nums[i]

        return result
