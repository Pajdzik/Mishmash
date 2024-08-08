#!/bin/python3
# https://leetcode.com/problems/spiral-matrix-iii
from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        result = []

        level = 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = rStart, cStart

        while len(result) < rows * cols:
            for dr, dc in directions:
                for _ in range(level):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    r = r + dr
                    c = c + dc

                if dc == 0:
                    level += 1

        return result


if __name__ == "__main__":

    def test_solution(
        rows: int, cols: int, rStart: int, cStart: int, expected: List[List[int]]
    ):
        solution = Solution()
        result = solution.spiralMatrixIII(rows, cols, rStart, cStart)
        assert result == expected, f"{result} != {expected}"

    # +----+----+----+----+----+----+
    # | 30 | 25 | 16 | 7  | 8  | 9  |
    # +----+----+----+----+----+----+
    # | 29 | 24 | 15 | 6  | 1  | 2  |
    # +----+----+----+----+----+----+
    # | 28 | 23 | 14 | 5  | 4  | 3  |
    # +----+----+----+----+----+----+
    # | 27 | 22 | 13 | 12 | 11 | 10 |
    # +----+----+----+----+----+----+
    # | 26 | 21 | 20 | 19 | 18 | 17 |
    # +----+----+----+----+----+----+
    test_solution(
        5,
        6,
        1,
        4,
        [
            [1, 4],
            [1, 5],
            [2, 5],
            [2, 4],
            [2, 3],
            [1, 3],
            [0, 3],
            [0, 4],
            [0, 5],
            [3, 5],
            [3, 4],
            [3, 3],
            [3, 2],
            [2, 2],
            [1, 2],
            [0, 2],
            [4, 5],
            [4, 4],
            [4, 3],
            [4, 2],
            [4, 1],
            [3, 1],
            [2, 1],
            [1, 1],
            [0, 1],
            [4, 0],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0],
        ],
    )
    test_solution(1, 4, 0, 0, [[0, 0], [0, 1], [0, 2], [0, 3]])
