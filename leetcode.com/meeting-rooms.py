#!/bin/python3
# https://leetcode.com/problems/meeting-rooms

import functools

class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals = sorted(intervals, key=functools.cmp_to_key(lambda i1, i2: i1[0] - i2[0]))

        for i in range(0, len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True

    def canAttendMeetings_o2(self, intervals: list[list[int]]) -> bool:
        for i in range(0, len(intervals) - 1):
            for j in range(i + 1, len(intervals)):
                if not (intervals[i][0] >= intervals[j][1] \
                    or intervals[j][0] >= intervals[i][1]):
                    return False

        return True