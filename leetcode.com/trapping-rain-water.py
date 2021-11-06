#!/bin/python3
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, heights: list[int]) -> int:
        left_max = [ 0 for _ in range(len(heights)) ]
        right_max = [ 0 for _ in range(len(heights)) ]

        local_max = 0
        for i, height in enumerate(heights):
            local_max = max(local_max, height)
            left_max[i] = local_max

        local_max = 0
        for i, height in enumerate(reversed(heights)):
            local_max = max(local_max, height)
            right_max[len(heights) - 1 - i] = local_max

        result = 0
        for i, height in enumerate(heights):
            min_trap = min(left_max[i], right_max[i])
            trapped_water = max(0, min_trap - height)
            result += trapped_water

        return result
