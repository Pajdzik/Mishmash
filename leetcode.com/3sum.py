#!/bin/python3
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        for i in range(0, len(nums) - 1):
            target = -nums[i]
            cache = set()

            for j in range(i + 1, len(nums)):
                value = target - nums[j]
                if value in cache:
                    sorted_result = sorted([nums[i], nums[j], value])
                    if sorted_result not in result:
                        result.append(sorted_result)
                else:
                    cache.add(nums[j])

        return result

Solution().threeSum([-1,0,1,2,-1,-4])