#!/bin/python3
#https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        level = 0

        for log in logs:
            if log == "../":
                if level > 0:
                    level -= 1
            elif log == "./":
                continue
            else:
                level += 1

        return level

steps = Solution().minOperations(["./","../","./"])