#!/bin/python3
# https://leetcode.com/problems/max-increase-to-keep-city-skyline

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        max_in_cols = [
            max([grid[row][col] for row in range(len(grid))])
            for col in range(len(grid[0]))
        ]

        max_in_rows = [
            max([grid[row][col] for col in range(len(grid[0]))])
            for row in range(len(grid))
        ]

        result = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                result += min(max_in_cols[col], max_in_rows[row]) - grid[row][col]

        return result


if __name__ == "__main__":

    def test(expected: int, grid: List[List[int]]):
        s = Solution()
        result = s.maxIncreaseKeepingSkyline(grid)
        assert result == expected, f"{result=}, {expected=}, {grid=}"

    test(35, [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
