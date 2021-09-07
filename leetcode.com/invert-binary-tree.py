#!/bin/python3
# https://leetcode.com/problems/invert-binary-tree/

from tkinter.tix import Tree
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invert_node(self, node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        self.invert_node(node.left)
        self.invert_node(node.right)

        node.left, node.right = node.right, node.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert_node(root)
        return root