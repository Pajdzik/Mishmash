#!/bin/python3
# https://leetcode.com/problems/merge-intervals/

import functools

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=functools.cmp_to_key(lambda i1, i2: i1[0] - i2[0]))

        result = []
        i = 0

        while i < len(intervals):
            end = intervals[i][1]

            j = i
            while j + 1 < len(intervals) and end >= intervals[j + 1][0]:
                end = max(end, intervals[j + 1][1])
                j += 1

            result.append([intervals[i][0], end])
            i = j + 1

        return result

Solution().merge([[1,3],[2,6],[8,10],[15,18]])
        