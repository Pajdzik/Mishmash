#!/bin/python3
# https://leetcode.com/problems/path-sum/

from tkinter.tix import Tree
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) \
            or self.hasPathSum(root.right, targetSum - root.val)

# root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
root = TreeNode(1, TreeNode(2))
result = Solution().hasPathSum(root, 1)
print(result) 