#!/bin/python3
# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return -1

        return 1 + max(self.get_height(node.left), self.get_height(node.right))
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        return abs(self.get_height(root.left) - self.get_height(root.right)) <= 1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)