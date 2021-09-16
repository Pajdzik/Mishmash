#!/bin/python3
# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        color = image[sr][sc]
        queue = [ (sr, sc) ]
        visited = set()

        while len(queue) > 0:
            r, c = queue.pop()

            if (r, c) in visited:
                continue
            else:
                visited.add((r, c))

            if not 0 <= r < len(image):
                continue

            if not 0 <= c < len(image[0]):
                continue

            if image[r][c] != color:
                continue

            image[r][c] = newColor

            for r_delta, c_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                queue.append((r + r_delta, c + c_delta))

        return image

Solution().floodFill([[0,0,0],[0,1,1]], 1, 1, 1)