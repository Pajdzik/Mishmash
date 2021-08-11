#!/bin/python3
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(node: Optional[TreeNode], order: list[TreeNode]):
    if not node:
        return

    order.append(node)
    preorder(node.left, order)
    preorder(node.right, order)
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        order = [ ]
        preorder(root, order)

        for i in range(len(order) - 1):
            order[i].right = order[i + 1]
            order[i].left = None

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
Solution().flatten(root)