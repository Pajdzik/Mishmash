#!/bin/python3
# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/description/

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class GraphNode:
     def __init__(self, val=0, neighbors=None):
         self.val = val
         self.neighbors = neighbors if neighbors else []
         self.is_leaf = False
        
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph: dict[int, GraphNode] = {}

        def convert(node: TreeNode, parent: GraphNode):
            graph_node = GraphNode(node.val)

            if parent:
                graph_node.neighbors.append(parent)
            if node.left:
                left_node = convert(node.left, graph_node)
                graph_node.neighbors.append(left_node)
            if node.right:
                right_node = convert(node.right, graph_node)
                graph_node.neighbors.append(right_node)

            graph_node.is_leaf = not node.left and not node.right
            graph[node.val] = graph_node
            return graph_node

        convert(root, None)

        start = graph[k]
        visited = {}
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node.val in visited:
                continue

            visited[node.val] = True

            if node.is_leaf:
                return node.val
            
            queue.extend(node.neighbors)



if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2))
    assert(Solution().findClosestLeaf(root, 1) == 2)

    root = TreeNode(1)
    assert(Solution().findClosestLeaf(root, 1) == 1)

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    Solution().findClosestLeaf(root, 1)