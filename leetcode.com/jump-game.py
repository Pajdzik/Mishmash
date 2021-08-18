#!/bin/python3
# https://leetcode.com/problems/jump-game/

def jump(nums: list[int], index: int) -> bool:
    if index >= len(nums):
        return True
        
    delta = nums[index]

    if index + delta == len(nums) - 1:
        return True

    while delta > 0:
        if jump(nums, index + delta):
            return True

        delta -= 1

    return False

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        target = len(nums) - 1

        for i in range(target - 1, -1, -1):
            if i + nums[i] >= target:
                target = i

            if target <= 0:
                return True

        return target <= 0

    def canJump_recursion(self, nums: list[int]) -> bool:
        return jump(nums, 0)


Solution().canJump([1])
