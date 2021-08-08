#!/bin/python3
# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        m = len(nums)
        visited = [ False for _ in range(m) ]

        for num in nums:
            if visited[num]:
                return num
            else:
                visited[num] = True