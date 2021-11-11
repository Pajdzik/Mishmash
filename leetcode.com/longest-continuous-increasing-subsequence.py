#!/bin/python3
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, numbers: list[int]) -> int:
        max_length = 0
        start = 0
        end = 0
        
        while start < len(numbers) and end < len(numbers):
            max_length = max(max_length, end - start + 1)

            if end + 1 < len(numbers) and numbers[end] < numbers[end + 1]:
                end += 1
            else:
                start = end + 1
                end = start

        return max_length