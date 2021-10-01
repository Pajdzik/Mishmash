#!/bin/python3
# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [ 1 for _ in range(rowIndex + 1) ]

        value = 1
        for i in range(1, rowIndex // 2 + 1):
            value = (value * (rowIndex - i  + 1)) //  i
            result[i] = value

        for i in range(rowIndex // 2 + 1, rowIndex + 1):
            result[i] = result[rowIndex - i]

        return result