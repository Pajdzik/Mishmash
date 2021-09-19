#!/bin/python3
# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0

        if len(intervals) == 0:
            return [newInterval]

        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
            i += 1

        if i == len(intervals):
            result.append(newInterval)
            return result
        elif i == 0 and len(intervals) > 0 and newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        interval_start, interval_end = newInterval

        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            interval_start = min(intervals[i][0], interval_start)
            interval_end = max(intervals[i][1], interval_end)
            i += 1
        
        result.append([interval_start, interval_end])

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
        
Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8])