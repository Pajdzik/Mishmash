#!/bin/python3
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

from operator import le
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = [root]
        left_first = True

        while queue:
            queue_vals = [n.val for n in queue if n is not None]
            if len(queue_vals) > 0:
                result.append(queue_vals if left_first else list(reversed(queue_vals)))

            new_queue = []

            for node in queue:
                if not node:
                    continue

                new_queue.append(node.left)
                new_queue.append(node.right)

            left_first = not left_first
            queue = new_queue

        return result


if __name__ == "__main__":

    def tree_from_array(nums: List[int]) -> TreeNode:
        root = TreeNode(nums[0])
        queue = [root]
        i = 1

        while queue and i < len(nums):
            node = queue.pop()
            if not node:
                continue

            if i < len(nums) and nums[i] is not None:
                node.left = TreeNode(nums[i])
                queue.append(node.left)
            i += 1

            if i < len(nums) and nums[i] is not None:
                node.right = TreeNode(nums[i])
                queue.append(node.right)
            i += 1

        return root

    assert Solution().zigzagLevelOrder(
        tree_from_array([1, 2, 3, 4, None, None, 5])
    ) == [[1], [3, 2], [4, 5]]
