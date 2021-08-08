#!/bin/python3
# https://leetcode.com/problems/search-insert-position/

def binary_search(nums: list[int], left: int, right: int, target: int) -> int:
    middle = max(left + ((right - left) // 2), 0)
    element = nums[middle]

    if element == target:
        return middle
    elif right <= left:
        if target > element:
            return middle + 1
        else:
            return middle
    elif target > element:
        return binary_search(nums, middle + 1, right, target)
    else:
        return binary_search(nums, left, middle - 1, target)

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return binary_search(nums, 0, len(nums) - 1, target)

Solution().searchInsert([1,3], 0)