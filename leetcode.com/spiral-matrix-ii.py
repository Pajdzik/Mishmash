#!/bin/python3
# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[None] * n for _ in range(n)]

        current_dir = 0
        current_value = 1
        current_row = 0
        current_col = -1

        def get_dir(
        ) -> tuple[int, int]: return directions[current_dir % len(directions)]

        while current_value <= n * n:
            diff_row, diff_col = get_dir()
            if not (0 <= current_row + diff_row < n) or \
                    not (0 <= current_col + diff_col < n) or \
                    result[current_row + diff_row][current_col + diff_col] != None:
                current_dir += 1
                diff_row, diff_col = get_dir()

            current_row += diff_row
            current_col += diff_col

            result[current_row][current_col] = current_value
            current_value += 1

        return result


if __name__ == "__main__":
    def test_and_print_failure(n: int, expected: list[list[int]]):
        result = Solution().generateMatrix(3)

        if result != expected:
            print(result)

    test_and_print_failure(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
