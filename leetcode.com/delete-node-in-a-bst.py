#!/bin/python3
# https://leetcode.com/problems/delete-node-in-a-bst

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_substitute_node(node: TreeNode) -> Optional[TreeNode]:
            while node and node.left:
                node = node.left

            return node

        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None:
                return None

            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            sub_node = find_substitute_node(root.right)
            root.val = sub_node.val
            root.right = self.deleteNode(root.right, sub_node.val)

        return root


if __name__ == "__main__":

    def test(expected: Optional[TreeNode], root: Optional[TreeNode], key: int):
        s = Solution()
        result = s.deleteNode(root, key)
        assert result == expected, f"{result=}, {expected=}, {root=}, {key=}"

    # test(TreeNode(1), TreeNode(2, TreeNode(1)), 2)
    # test(None, TreeNode(0), 0)

    test(
        None,
        TreeNode(
            5,
            left=TreeNode(
                3,
                left=TreeNode(2),
                right=TreeNode(4),
            ),
            right=TreeNode(
                6,
                right=TreeNode(7),
            ),
        ),
        7,
    )

    test(
        None,
        TreeNode(
            5,
            left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)),
            right=TreeNode(6, right=TreeNode(7)),
        ),
        3,
    )
