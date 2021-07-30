#!/bin/python3
# https://leetcode.com/problems/rotate-array/

def flip(nums: list[int], start: int, end: int) -> None:
    for i in range(0, (end - start) // 2 + 1):
        nums[start + i], nums[end - i] = nums[end - i], nums[start + i]

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        flip(nums, 0, len(nums) - 1)
        flip(nums, 0, k - 1)
        flip(nums, k, len(nums) - 1)

Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)