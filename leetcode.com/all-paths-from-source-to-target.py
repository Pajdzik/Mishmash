#!/bin/python3
# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        result = []
        queue = [(0, [0])]

        while queue:
            node_index, path = queue.pop()

            for target_node in graph[node_index]:
                if target_node == target:
                    result.append(path + [target_node])
                else:
                    queue.append((target_node, path + [target_node]))

        return result

        
if __name__ == "__main__":
    Solution().allPathsSourceTarget([[1,2],[3],[3],[]])