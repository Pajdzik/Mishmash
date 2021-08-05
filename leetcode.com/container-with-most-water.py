#!/bin/python3
# https://leetcode.com/problems/container-with-most-water/

from operator import le


def get_area(heights: list[int], left: int, right: int):
    return (right - left) * min(heights[left], heights[right])

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while right > left:
            area = (right - left) * min(heights[right], heights[left])
            max_area = max(max_area, area)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return max_area

Solution().maxArea([1,3,2,5,25,24,5])