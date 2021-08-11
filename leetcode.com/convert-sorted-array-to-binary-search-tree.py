#!/bin/python3
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(nums: list[int], left: int, right: int) -> TreeNode:
    if left > right:
        return None

    middle = left + ((right - left) // 2)
    root = TreeNode(nums[middle])
    
    root.left = insert(nums, left, middle - 1)
    root.right = insert(nums, middle + 1, right)

    return root

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        root = insert(nums, 0, len(nums) - 1)
        return root


Solution().sortedArrayToBST(range(15))