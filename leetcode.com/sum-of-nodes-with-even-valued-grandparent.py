#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def sum(
            node: Optional[TreeNode],
            parent: Optional[TreeNode],
            grandparent: Optional[TreeNode],
        ):
            if not node:
                return 0

            if not parent or not grandparent or grandparent.val % 2 != 0:
                return sum(node.left, node, parent) + sum(node.right, node, parent)

            return (
                node.val + sum(node.left, node, parent) + sum(node.right, node, parent)
            )

        return sum(root, None, None)


if __name__ == "__main__":
    pass
