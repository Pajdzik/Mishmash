#!/bin/python3
# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle

from math import sqrt
from typing import List
from unittest import result


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        result = []

        for query in queries:
            x_circle, y_circle, r = query
            count = 0

            for point in points:
                x_point, y_point = point

                x_diff = x_point - x_circle
                y_diff = y_point - y_circle
                dist = sqrt(x_diff**2 + y_diff**2)
                if r >= dist:
                    count += 1

            result.append(count)

        return result


if __name__ == "__main__":

    def test_solution(
        expected: List[int], points: List[List[int]], queries: List[List[int]]
    ):
        s = Solution()
        result = s.countPoints(points, queries)
        assert result == expected, f"expected {expected}, but got {result}"

    test_solution(
        [3, 2, 2], [[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    )
