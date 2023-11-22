#!/bin/python3
# https://leetcode.com/problems/deepest-leaves-sum/

from collections import Counter
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            sum = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return sum

    def deepestLeavesSum_with_map(self, root: Optional[TreeNode]) -> int:
        sums = {}
        queue = [(root, 0)]

        while queue:
            node, depth = queue.pop()

            if sums.get(depth) is None:
                sums[depth] = []

            sums[depth].append(node.val)

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

        max_depth = max(sums.keys())
        return sum(sums[max_depth])
