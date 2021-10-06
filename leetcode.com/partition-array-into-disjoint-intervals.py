#!/bin/python3
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

from logging import root


class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
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

    def partitionDisjoint__foo(self, nums: list[int]) -> int:
        left, max_left = 0, nums[0]
        right, min_right = 1, nums[1]

        while True:
            for i in range(left + 1):
                if nums[i] >= max_left:
                    left, max_left = i, nums[i]
            
            for i in range(right, len(nums)):
                if nums[i] < min_right:
                    right, min_right = i, nums[i]

            if min_right >= max_left:
                return right

            if nums[left] <= nums[right]:
                max_left = nums[right]

            left = right
            right = right + 1
            min_right = nums[right]

Solution().partitionDisjoint([5,0,3,8,6])