#!/bin/python3
# https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]


if __name__ == "__main__":
    def test(expected: list[list[int]], matrix: list[list[int]]):
        result = Solution().transpose(matrix)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test([[1, 4], [2, 5], [3, 6]], [[1, 2, 3], [4, 5, 6]])
