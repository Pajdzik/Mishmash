#!/bin/python3
# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        path_map = {}

        for path in paths:
            origin, destination = path

            if origin not in path_map:
                path_map[origin] = []

            path_map[origin].append(destination)

        queue = [paths[0][0]]

        while queue:
            origin = queue.pop()
            if origin not in path_map:
                return origin

            queue.extend(path_map[origin])
