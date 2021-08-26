#!/bin/python3
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []

        for level in range(0, numRows):
            row = []
            for i in range(0, level + 1):
                if i == 0 or i == level:
                    row.append(1)
                else:
                    row.append(result[level - 1][i - 1] + result[level - 1][i])

            result.append(row)

        return result

Solution().generate(5)