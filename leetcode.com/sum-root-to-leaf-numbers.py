#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], number: int) -> int:
            next_number = number * 10 + node.val
            if not node.left and not node.right:
                return next_number

            left_path = traverse(node.left, next_number) if node.left else 0
            right_path = traverse(node.right, next_number) if node.right else 0

            return left_path + right_path

        return traverse(root, 0)


if __name__ == "__main__":
    assert Solution().sumNumbers(TreeNode(0, TreeNode(1))) == 1
    assert Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25
