#!/bin/python3
# https://leetcode.com/problems/symmetric-tree/

from tkinter.tix import Tree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_queue = [ root.left ]
        right_queue = [ root.right ]

        while len(left_queue) > 0 or len(right_queue) > 0:
            left_node = left_queue.pop(0)
            rigth_node = right_queue.pop(0)

            if left_node is None and rigth_node is None:
                continue
            elif left_node is None or rigth_node is None:
                return False
            elif left_node.val != rigth_node.val:
                return False

            left_queue.append(left_node.left)
            left_queue.append(left_node.right)
            right_queue.append(rigth_node.right)
            right_queue.append(rigth_node.left)
            
        return True

root = TreeNode(1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3)))

Solution().isSymmetric(root)