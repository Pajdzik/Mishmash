#!/bin/python3
# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[middle + 1]:
                right = middle
            else:
                left = middle + 1

        return left