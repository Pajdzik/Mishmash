#!/bin/python3
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = -9999999
        local_max_sum = -9999999
        for num in nums:
            local_max_sum = max(num, local_max_sum + num)
            if local_max_sum > max_sum:
                max_sum = local_max_sum

        return max_sum