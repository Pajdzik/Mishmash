#!/bin/python3
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        edges_map = {i: [] for i in range(n)}

        for edge in edges:
            from_node, to_node = edge
            edges_map[to_node].append(from_node)

        result = []

        for to_node in range(n):
            ancestors = []
            visited = set()
            queue = [*edges_map[to_node]]

            while queue:
                ancestor = queue.pop()
                if ancestor in visited:
                    continue
                visited.add(ancestor)
                ancestors.append(ancestor)
                queue.extend(edges_map[ancestor])

            result.append(sorted(ancestors))

        return result


if __name__ == "__main__":

    def test(expected: list[list[int]], n: int, edges: list[list[int]]):
        result = Solution().getAncestors(n, edges)
        assert result == expected, f"expected {expected}, but got {result}"

    test(
        [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]],
        8,
        [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]],
    )
