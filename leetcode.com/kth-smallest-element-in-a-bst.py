#!/bin/python3
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []

        def in_order(node: TreeNode):
            if not node:
                return
            if len(order) > k:
                return
            in_order(node.left)
            order.append(node.val)
            in_order(node.right)

        in_order(root)
        return order[k]


if __name__ == "__main__":
    def test_and_print_failure(root: TreeNode, k: int, expected: int):
        res = Solution().kthSmallest(root, k)

        if res != expected:
            print(f'Incorrect result for {k}: {res}')

    test_1 = TreeNode(5, TreeNode(3, TreeNode(
        2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    test_and_print_failure(test_1, 3, 3)
