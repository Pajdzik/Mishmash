#!/bin/python3
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set = {}
        
        for num in nums1:
            if num in set:
                continue
            else:
                set[num] = False

        result = []
        for num in nums2:
            if num in set and not set[num]:
                result.append(num)
                set[num] = True

        return result