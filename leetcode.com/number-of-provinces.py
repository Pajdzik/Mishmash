#!/bin/python3
# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        provinces_count = 0
        visited = set()

        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if r in visited:
                    continue
                
                provinces_count += 1
                queue = [ r ]
                
                while queue:
                    source_node = queue.pop()
                    if source_node in visited:
                        continue
                    else:
                        visited.add(source_node)

                    for target_node, is_connected in enumerate(isConnected[source_node]):
                        if is_connected == 1: 
                            queue.append(target_node)

        return provinces_count

    def findCircleNum_with_map(self, isConnected: list[list[int]]) -> int:
        map = { i: set() for i in range(len(isConnected))}

        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c] == 0 or r == c:
                    continue

                if r in map and c in map[r]:
                    continue
                else:
                    map[r].add(c)
                    map[c].add(r)

        provinces_count = 0
        visited = set()

        for node in map.keys():
            if node not in visited:
                provinces_count += 1

                queue = [ node ]
                while queue:
                    visited_node = queue.pop()
                    if visited_node not in visited:
                        visited.add(visited_node)

                        for target_node in map[visited_node]:
                            queue.append(target_node)

        return provinces_count

if __name__ == "__main__":
    Solution().findCircleNum([[1]])