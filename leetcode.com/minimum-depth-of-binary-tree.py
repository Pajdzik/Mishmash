#!/bin/python3
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        queue = [ (root, 0) ]

        while len(queue) > 0:
            node, height = queue.pop(0)

            if node.left == None and node.right == None:
                return height + 1

            if node.left:
                queue.append((node.left, height + 1))
            if node.right:
                queue.append((node.right, height + 1))