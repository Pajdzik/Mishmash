#!/bin/python3
# https://leetcode.com/problems/shortest-word-distance/

class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        placements = {}

        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word in placements:
                placements[word].append(i)
            else:
                placements[word] = [ i ]

        min_dist = len(wordsDict)

        for i1 in placements[word1]:
            for i2 in placements[word2]:
                min_dist = min(min_dist, abs(i1 - i2))

        return min_dist