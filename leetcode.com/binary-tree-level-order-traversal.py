#!/bin/python3
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        result = []
        level = [ root ]

        while level:
            result_level = []
            for node in level:
                result_level.append(node.val)
            result.append(result_level)

            queue = []
            while level:
                node = level.pop(0)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level = queue

        return result

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
Solution().levelOrder(root)