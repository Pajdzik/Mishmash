#!/bin/python3
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        left_max = nums[0]
        right_max = nums[0]
        split = 1

        for i in range(1, len(nums)):
            if nums[i] < left_max:
                split = i + 1
                left_max = right_max
            else:
                right_max = max(right_max, nums[i])

        return split

    def partitionDisjoint_additional_memory(self, nums: list[int]) -> int:
        minimums = [ None ] * len(nums)
        maximums = [ None ] * len(nums)

        minimum = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            minimum = min(minimum, nums[i])
            minimums[i] = minimum

        maximum = nums[0]
        for i in range(len(nums)):
            maximum = max(maximum, nums[i])
            maximums[i] = maximum
        
        i = 0
        while maximums[i] > minimums[i + 1]:
            i += 1

        return i + 1  


Solution().partitionDisjoint([5,0,3,8,6])