#!/bin/python3
# https://leetcode.com/problems/average-of-levels-in-binary-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if not root:
            return []
        
        averages = []
        level_nodes = [root]

        while level_nodes:
            s = 0

            new_level = []
            for node in level_nodes:
                s += node.val
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            averages.append(s / len(level_nodes))
            level_nodes = new_level

        return averages
        
if __name__ == "__main__":
    def test(root: Optional[TreeNode], expected: list[float]):
        s = Solution()
        result = s.averageOfLevels(root)
        assert result == expected, f"For {root}, expected {expected} but got {result}"

    test(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [3.0, 14.5, 11.0])
    test(TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20)), [3.0, 14.5, 11.0])