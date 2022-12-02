#!/bin/python3
# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, el in enumerate(heights):
            while stack and heights[stack[-1]] >= el:
                hi = stack.pop()
                width = i - (stack[-1] if stack else -1) - 1
                max_area = max(max_area, heights[hi] * width)

            stack.append(i)

        width = 1
        while stack:
            hi = stack.pop()
            width = len(heights) - (stack[-1] if stack else -1) - 1
            max_area = max(max_area, heights[hi] * width)

        return max_area
 
    def get_min_height_recursion(self, heights: list[int], left: int, right: int) -> tuple[int, int]:
        min_height = heights[left]
        index = left

        for i in range(left + 1, right + 1):
            if heights[i] < min_height:
                min_height, index = heights[i], i

        return min_height, index

    def get_area(self, heights: list[int], left: int, right: int) -> int:
        if right < left:
            return 0
        if left == right:
            return heights[left]

        min_height, min_index = self.get_min_height(heights, left, right)
        left_area = self.get_area(heights, left, min_index - 1)
        right_area = self.get_area(heights, min_index + 1, right)

        return max(
            min_height * (right - left + 1), 
            left_area, 
            right_area
        )

    def largestRectangleArea_recursive(self, heights: List[int]) -> int:
        area = self.get_area(heights, 0, len(heights) - 1)
        return area

    def largestRectangleArea_bruteforce(self, heights: List[int]) -> int:
        max_areas = heights.copy()

        for i in range(0, len(heights)):
            local_max_area = heights[i]
            min_height = heights[i]
            
            for j in range(i - 1, -1, -1):
                min_height = min(min_height, heights[j])
                local_max_area = max(local_max_area, (i - j + 1) * min_height)
            
            max_areas[i] = local_max_area

        return max(max_areas)

if __name__ == "__main__":
    assert(Solution().largestRectangleArea([1, 1]) == 2)
    assert(Solution().largestRectangleArea([2,1,5,6,2,3]) == 10)