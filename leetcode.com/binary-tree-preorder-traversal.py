#!/bin/python3
# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder_recursive(self, node: Optional[TreeNode], list: list[int]) -> None:
        if node:
            list.append(node.val)
        else:
            return

        if node.left:
            self.preorder(node.left, list)
        
        if node.right:
            self.preorder(node.right, list)

    def preorder_iterative(self, root: Optional[TreeNode]):
        if not root:
            return []

        stack = [ root ]
        result = []

        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = self.preorder_iterative(root)
        return result