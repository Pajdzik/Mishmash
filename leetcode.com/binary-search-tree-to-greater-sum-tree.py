#!/bin/python3
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def foo(node: Optional[TreeNode], to_add: int) -> int:
            if not node:
                return to_add

            if not node.left and not node.right:
                node.val += to_add
                return node.val

            to_add_from_the_right_subtree = foo(node.right, to_add)
            node.val += to_add_from_the_right_subtree

            to_add_including_parent = node.val
            return foo(node.left, to_add_including_parent)

        foo(root, 0)
        return root


if __name__ == "__main__":

    def test_solution(root: TreeNode, expected: TreeNode):
        def serialize(node: TreeNode) -> str:
            if not node:
                return "null"

            return f"{node.val},{serialize(node.left)},{serialize(node.right)}"

        solution = Solution()
        result = solution.bstToGst(root)
        assert serialize(result) == serialize(
            expected
        ), f"{serialize(result)} != {serialize(expected)}"

    # root = TreeNode(
    #     4,
    #     TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))),
    #     TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))),
    # )

    # expected = TreeNode(
    #     30,
    #     TreeNode(36, TreeNode(36), TreeNode(35, None, TreeNode(33))),
    #     TreeNode(21, TreeNode(26), TreeNode(15, None, TreeNode(8))),
    # )

    #     3         7
    #    / \       / \
    #   2   4     9   4
    #  /         /
    # 1         10

    root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    expected = TreeNode(7, TreeNode(4, TreeNode(1)), TreeNode(9))

    test_solution(root, expected)
