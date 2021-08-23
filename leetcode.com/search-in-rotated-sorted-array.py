#!/bin/python3
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        shift = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                shift = len(nums) - i
                break
            
        left = 0
        right = len(nums) - 1

        while right >= left:
            middle = left + ((right - left) // 2)
            
            index = middle - shift
            if index < 0:
                index += len(nums)

            number = nums[index]
            if number > target:
                right = middle - 1
            elif number < target:
                left = middle + 1
            elif number == target:
                return index

        return -1

Solution().search([3,5,1], 5)