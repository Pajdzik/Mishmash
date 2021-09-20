#!/bin/python3
# https://leetcode.com/problems/triangle/

from inspect import trace


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for level in range(1, len(triangle)):
            for i in range(len(triangle[level])):
                existing_path1 = triangle[level - 1][i] if i < len(triangle[level - 1]) else 9999
                existing_path2 = triangle[level - 1][i - 1] if i > 0 else 99999
                existing_path_cost = min(existing_path1, existing_path2)
                path = existing_path_cost + triangle[level][i]
                triangle[level][i] = path

        min_path = min(triangle[-1])

        return min_path
                
Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])