#!/bin/python3
# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, columns = binaryMatrix.dimensions()

        result = -1
        for row in range(rows):
            start_column = result if result > -1 else columns - 1
            for column in range(start_column, -1, -1):
                value = binaryMatrix.get(row, column)
                if value == 1:
                    result = column
                else:
                    break

        return result