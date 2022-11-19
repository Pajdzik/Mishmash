#!/bin/python3
# https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # (max diameter, max signle path)
        def diameter_and_path(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return (0, -1)
            
            left_diameter, left_path = diameter_and_path(node.left)
            right_diameter, right_path = diameter_and_path(node.right)

            max_diameter = max(left_diameter, right_diameter, left_path + right_path + 2)
            max_path = max(left_path, right_path) + 1

            return max_diameter, max_path
        
        max_diameter, _ = diameter_and_path(root)
        return max_diameter
            
            