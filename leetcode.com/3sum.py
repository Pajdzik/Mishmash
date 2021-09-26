#!/bin/python3
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        seen = {}
        
        for i in range(len(nums)):
            a = nums[i]
            if a not in seen:
                seen[a] = i
            
            for j in range(i + 1, len(nums)):
                b = nums[j]
                c = -(nums[i] + nums[j])
                
                if c in seen and seen[c] != i != j:
                    result_three = tuple(sorted((a, b, c)))
                    if not result_three in result and i != j != seen[c]:
                        result.add(result_three)
                
                seen[b] = j
                
        return list(result)

Solution().threeSum([-1,0,1,2,-1,-4])