#!/bin/python3
# https://leetcode.com/problems/furthest-building-you-can-reach


import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        queue = []
        index = 0

        for index in range(1, len(heights)):
            height_diff = heights[index - 1] - heights[index]
            if height_diff >= 0:
                continue

            heapq.heappush(queue, height_diff)
            bricks += height_diff

            if bricks < 0:
                biggest_negative_height_diff = heapq.heappop(queue)
                bricks -= biggest_negative_height_diff
                ladders -= 1
                if ladders < 0:
                    return index - 1

        return index

    def furthestBuilding_recursion(self, heights: list[int], bricks: int, ladders: int) -> int:
        def calculateFarthestBuilding(index: int, bricks_used: int, ladders_used: int) -> int:
            if index >= len(heights) - 1:
                return index
            if heights[index + 1] <= heights[index]:
                return calculateFarthestBuilding(index + 1, bricks_used, ladders_used)
            if bricks_used == bricks and ladders_used == ladders:
                return index

            height_diff = heights[index + 1] - heights[index]
            bricks_distance = index
            if bricks - bricks_used >= height_diff:
                bricks_distance = calculateFarthestBuilding(
                    index + 1, bricks_used + height_diff, ladders_used)

            ladders_distance = index
            if ladders_used < ladders:
                ladders_distance = calculateFarthestBuilding(
                    index + 1, bricks_used, ladders_used + 1)

            return max(bricks_distance, ladders_distance)

        return calculateFarthestBuilding(0, 0, 0)


if __name__ == "__main__":
    def checkSolution(expected: int, heights: list[int], bricks: int, ladders: int):
        s = Solution()
        result = s.furthestBuilding(heights, bricks, ladders)
        assert result == expected, f"Expected {expected} but got {result}"

    checkSolution(4, [4, 2, 7, 6, 9, 14, 12], 5, 1)
    checkSolution(7, [4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2)
