#!/bin/python3
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) > 0:
            root_value = postorder.pop()
            root = TreeNode(root_value)

            split_index = inorder.index(root_value)

            root.right = self.buildTree(inorder[split_index + 1 :], postorder)
            root.left = self.buildTree(inorder[:split_index], postorder)

            return root
