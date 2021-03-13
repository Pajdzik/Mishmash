#!/bin/python3
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        pass

    def insert(root, value):
        parent = root

        if root.val < value:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                insert(root.left)
        else:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                insert(root.right)

