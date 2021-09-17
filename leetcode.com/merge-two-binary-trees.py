#!/bin/python3
# https://leetcode.com/problems/merge-two-binary-trees/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
        if node1 == None and node2 == None:
            return None

        new_node = TreeNode(0)
        new_node.val += node1.val if node1 else 0
        new_node.val += node2.val if node2 else 0

        node1_left, node1_right = (node1.left, node1.right) if node1 else (None, None)
        node2_left, node2_right = (node2.left, node2.right) if node2 else (None, None)

        new_node.left = self.mergeTrees(node1_left, node2_left)
        new_node.right = self.mergeTrees(node1_right, node2_right)

        return new_node

root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
