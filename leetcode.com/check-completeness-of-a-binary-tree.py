#!/bin/python3
# https://leetcode.com/problems/check-completeness-of-a-binary-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        missing_child = False

        while queue:
            node = queue.pop(0)
            if not node:
                missing_child = True
                continue

            if missing_child:
                return False

            queue.append(node.left)
            queue.append(node.right)

        return True


def main():
    # Test case 1: Complete binary tree
    assert (
        Solution().isCompleteTree(
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        )
        == True
    )

    # Test case 2: Incomplete binary tree
    assert (
        Solution().isCompleteTree(
            TreeNode(
                1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6))
            )
        )
        == False
    )

    # Test case 3: Single node tree
    assert Solution().isCompleteTree(TreeNode(1)) == True

    # Test case 4: Empty tree
    assert Solution().isCompleteTree(None) == True

    print("All test cases passed.")


if __name__ == "__main__":
    main()
