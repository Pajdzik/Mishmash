#!/bin/python3
# https://leetcode.com/problems/height-checker


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        return sum([1 if x != y else 0 for x, y in zip(heights, sorted(heights))])
