#!/bin/python3
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def binary_search(nums: list[int], start: int, end: int, target: int) -> int:
    middle_index = start + ((end - start) // 2)
    middle_value = nums[middle_index]

    if middle_value == target:
        return middle_index
    elif start >= end:
        return - 1
    elif middle_value > target:
        return binary_search(nums, 0, middle_index - 1, target)
    elif middle_value < target:
        return binary_search(nums, middle_index + 1, end, target)

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]

        target_index = binary_search(nums, 0, len(nums) - 1, target)
        
        if target_index == -1:
            return [-1, -1]

        min_index = target_index
        for i in range(target_index, -1, -1):
            if nums[i] == target:
                min_index = i 
            else:
                break

        max_index = target_index
        for i in range(target_index, len(nums)):
            if nums[i] == target:
                max_index = i
            else:
                break

        return [min_index, max_index]

Solution().searchRange([1,1,2], 1)