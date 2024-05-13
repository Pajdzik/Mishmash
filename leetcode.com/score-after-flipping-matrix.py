#!/bin/python3
#https://leetcode.com/problems/score-after-flipping-matrix

from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        col_flip_threshold = (len(grid) + 1) // 2

        flipped_rows = [1 if el[0] == 0 else 0 for el in grid]

        def count_zeroes(column_index: int) -> int:
            count = 0
            for r in range(len(grid)):
                if (grid[r][column_index] ^ flipped_rows[r]) == 0:
                    count += 1
            return count

        flipped_cols = [1 if count_zeroes(c) >= col_flip_threshold else 0 for c in range(len(grid[0]))]

        def convert_from_binary(row_index: int) -> int:
            result = 0

            for col_index, b in enumerate(grid[row_index]):
                result = result << 1

                b = b ^ flipped_rows[row_index]
                b = b ^ flipped_cols[col_index]
                result = result | b

            return result

        converted_numbers = [convert_from_binary(r) for r in range(len(grid))]
        return sum(converted_numbers)
    
if __name__ == "__main__":
    def test(value, expect):
        s = Solution()
        assert s.matrixScore(value) == expect

    test([[0,0,1,1],[1,0,1,0],[1,1,0,0]], 39)

"""
0 0 1 1
1 0 1 0
1 1 0 0

Changing the first row
1 1 0 0
1 0 1 0
1 1 0 0

Changing the third column
1 1 1 0
1 0 0 1
1 1 1 0

Chaging the fourth column
1 1 1 1
1 0 0 0
1 1 1 1
"""
