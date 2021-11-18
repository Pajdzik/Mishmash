#!/bin/python3
# https://leetcode.com/problems/bus-routes/

from collections import deque

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_line = { }

        for line_number, route in enumerate(routes):
            for stop in route:
                if stop not in stop_to_line:
                    stop_to_line[stop] = set()

                stop_to_line[stop].add(line_number)

        start_lines = stop_to_line[source]
        queue = deque()

        for line in start_lines:
            queue.append((line, 1))

        visited = set()

        while queue:
            line, transfer_count = queue.popleft()
            if line in visited:
                continue
            if target in routes[line]:
                return transfer_count
       
            visited.add(line)

            for stop in routes[line]:
                for line in stop_to_line[stop]:
                    queue.append((line, transfer_count + 1))

        return -1


if __name__ == "__main__":
    assert(Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6) == 2)