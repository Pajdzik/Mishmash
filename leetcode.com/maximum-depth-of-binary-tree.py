#!/bin/python3
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        max_depth = 0
        stack = [ (root, 1) ]
        
        while len(stack) > 0:
            (node, depth) = stack.pop()

            if node.left != None:
                stack.append((node.left, depth + 1))
            
            if node.right != None:
                stack.append((node.right, depth + 1))

            if node.left == node.right == None:
                max_depth = max(max_depth, depth)

        return max_depth