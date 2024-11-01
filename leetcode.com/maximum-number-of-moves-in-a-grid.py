#!/bin/python3
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid

from typing import List

#     2,  4,  3,  5
#     5,  4,  9,  3
#     3,  4,  2, 11
#    10,  9, 13, 15


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        paths = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(len(grid)):
            paths[r][0] = 1

        def check_prev_column(row: int, col: int):
            max_path = 0
            for row_delta in [-1, 0, 1]:
                row_to_check = row + row_delta
                if not 0 <= row_to_check < len(grid):
                    continue
                prev_col = col - 1
                if not 0 <= prev_col:
                    continue

                curr_value = grid[row][col]
                prev_value = grid[row_to_check][prev_col]
                if prev_value >= curr_value or paths[row_to_check][prev_col] == 0:
                    continue

                paths[row][col] = max(
                    paths[row][col], paths[row_to_check][prev_col] + 1
                )
                max_path = max(max_path, paths[row][col])

            return max_path

        result = 0
        for col in range(1, len(grid[0])):
            for row in range(len(grid)):
                result = max(check_prev_column(row, col), result)

        return max(result - 1, 0)

    def maxMoves_bfs(self, grid: List[List[int]]) -> int:
        def find_next_steps(row: int, col: int) -> List[int]:
            steps = []
            for row_delta in [-1, 0, 1]:
                next_row = row + row_delta
                if not 0 <= next_row < len(grid):
                    continue
                next_col = col + 1
                if not 0 <= next_col < len(grid[0]):
                    continue

                curr_value = grid[row][col]
                next_value = grid[next_row][next_col]

                if next_value > curr_value:
                    steps.append((next_row, next_col))

            return steps

        def traverse() -> int:
            max_single_path = 0
            queue = [(r, 0, -1) for r in range(len(grid))]
            visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

            while queue:
                row, col, length = queue.pop(0)
                if visited[row][col]:
                    continue
                visited[row][col] = True
                next_steps = find_next_steps(row, col)
                max_single_path = max(max_single_path, length + 1)
                queue.extend([(r, c, length + 1) for (r, c) in next_steps])

            return max_single_path

        result = traverse()

        return result


if __name__ == "__main__":

    def test(expected: int, grid: List[List[int]]):
        s = Solution()
        result = s.maxMoves(grid)
        assert result == expected, f"{result=}, {expected=}, {grid=}"

    test(3, [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]])
