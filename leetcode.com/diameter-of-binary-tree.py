#!/bin/python3
# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calc_diameter(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return (-1, 0)
                    
            left_path, left_max = calc_diameter(node.left)
            right_path, right_max = calc_diameter(node.right)

            max_path = max(left_path, right_path)
            max_diameter = max(left_max, right_max, left_path + right_path + 2)

            return max_path + 1, max_diameter

        _, result = calc_diameter(root)

        return result

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert(Solution().diameterOfBinaryTree(root) == 3)