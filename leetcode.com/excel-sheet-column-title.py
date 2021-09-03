#!/bin/python3
# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = [ chr(i) for i in range(ord('A'), ord('Z') + 1)]
        result = []

        while columnNumber > 0:
            result.insert(0, d[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26

        return ''.join(result)

res = Solution().convertToTitle(28)
print(res)