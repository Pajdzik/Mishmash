#!/bin/python3
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) > 0:
            root_value = preorder.pop(0)
            root = TreeNode(root_value)

            split_index = inorder.index(root_value)

            root.left = self.buildTree(preorder, inorder[:split_index])
            root.right = self.buildTree(preorder, inorder[split_index + 1 :])

            return root
