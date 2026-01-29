#!/bin/python3
# https://leetcode.com/problems/maximum-binary-tree/description/

from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def max_with_index(start: int, end: int) -> Tuple[int, int]:
            max, index = -1, -1
            for i in range(start, end):
                if nums[i] > max:
                    max, index = nums[i], i

            return (index, max)

        def recurse(start: int, end: int):
            if start >= end:
                return None
            index, value = max_with_index(start, end)

            left_node = recurse(start, index)
            right_node = recurse(index + 1, end)

            return TreeNode(value, left_node, right_node)

        return recurse(0, len(nums))


if __name__ == "__main__":
    Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
