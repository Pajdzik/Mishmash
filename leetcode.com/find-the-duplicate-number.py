#!/bin/python3
# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate_bst(self, nums: list[int]) -> int:
        low = 1
        high = len(nums) - 1
        
        while low < high:
            middle = low + ((high - low) // 2)
            count = 0

            for num in nums:
                if num <= middle:
                    count += 1

            if count > middle:
                high = middle
            else:
                low = middle + 1

        return low

    def findDuplicate_map(self, nums: list[int]) -> int:
        m = len(nums)
        visited = [ False for _ in range(m) ]

        for num in nums:
            if visited[num]:
                return num
            else:
                visited[num] = True