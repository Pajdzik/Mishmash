#!/bin/python3
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter = {}
        for num in nums1:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        result = []
        for num in nums2:
            if num in counter:
                if counter[num] == 1:
                    del counter[num]
                else:
                    counter[num] -= 1
                
                result.append(num)

        return result