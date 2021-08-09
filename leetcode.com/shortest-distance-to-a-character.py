#!/bin/python3
# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        indices = []
        for i, el in enumerate(s):
            if el == c:
                indices.append(i)

        closest = 0
        result = []
        for i, el in enumerate(s):
            dist = abs(i - indices[closest])
            if (closest + 1) < len(indices):
                new_dist = abs(i - indices[closest + 1])
                if new_dist <= dist:
                    dist = new_dist
                    closest += 1

            result.append(dist)

        return result