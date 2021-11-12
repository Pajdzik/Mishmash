#!/bin/python3
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def find_max_path(node: Optional[TreeNode]):
            nonlocal max_sum

            if not root:
                return 0

            left_path_sum = max(0, find_max_path(root.left))
            right_path_sum = max(0, find_max_path(root.right))

            whole_path_sum = root.val + left_path_sum + right_path_sum
            max_sum = max(max_sum, whole_path_sum)

            return root.val + max(left_path_sum, right_path_sum)

        find_max_path(root)
        return max_sum

if __name__ == "__main__":
    root = TreeNode(-3)
    assert(Solution().maxPathSum(root) == -3)

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert(Solution().maxPathSum(root) == 6)