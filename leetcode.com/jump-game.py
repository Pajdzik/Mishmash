#!/bin/python3
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        last_position = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i

        return last_position <= 0

    def canJump_topbottom(self, nums: list[int]) -> bool:
        status = [ None for _ in range(len(nums)) ]
        
        status[len(nums) - 1] = True
        for i in range(len(nums) - 2, -1, -1):
            can_reach = False

            for j in range(i, min(i + nums[i] + 1, len(nums))):
                if status[j]:
                    can_reach = True
                    break
            
            status[i] = can_reach

        return status[0]

Solution().canJump([2,3,1,1,4])