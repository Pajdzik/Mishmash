#!/bin/python3
# https://leetcode.com/problems/rotate-array/

def flip(nums: list[int], start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        flip(nums, 0, len(nums) - 1)
        flip(nums, 0, k - 1)
        flip(nums, k, len(nums) - 1)

Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)