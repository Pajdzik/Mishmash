#!/bin/python3
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        map = { chr(c): c- ord('A') + 1 for c in range(ord('A'), ord('Z') + 1) }

        column = 0

        for i in range(0, len(columnTitle)):
            column *= len(map)
            column += map[columnTitle[i]]

        return column

Solution().titleToNumber('ZY')