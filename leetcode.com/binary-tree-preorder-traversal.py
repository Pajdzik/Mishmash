#!/bin/python3
# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, node: Optional[TreeNode], list: list[int]) -> None:
        if node:
            list.append(node.val)
        else:
            return

        if node.left:
            self.preorder(node.left, list)
        
        if node.right:
            self.preorder(node.right, list)

    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        self.preorder(root, result)
        return result