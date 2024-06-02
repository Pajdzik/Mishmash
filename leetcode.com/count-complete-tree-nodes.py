#!/bin/python3
# https://leetcode.com/problems/count-complete-tree-nodes

from typing import Optional

#            1
#         /    \
#        2      3
#      /  \    /  \
#     4    5  6    7
#    / \
#   8   9

#     1
#    /  \
#   2    3
#  / \  /
# 4  5 6

# Height: 3
# Count of the nodes without nodes at the last level: 3
# Last level: 3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_height(node: Optional[TreeNode], height: int = 0):
            if not node:
                return height
            return get_height(node.left, height + 1)

        def count_inclusive_nodes(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_subtree_height = get_height(node.left)
            right_subtree_height = get_height(node.right)

            if left_subtree_height == right_subtree_height:
                # Left subtree is full as there is at least one element
                # in the right subtree that goes as deep as the elements in the left subtree.
                # Thus, we don't have to count elements in the left subtree.

                left_subtree_count = 2**left_subtree_height - 1
                return 1 + left_subtree_count + count_inclusive_nodes(node.right)
            else:
                # Left subtree is deeper than the left-most element in the right subtree.
                # That means the last node at the last level is on the left side, which
                # subsequently means the right tree is full (and one level shallower then the left).
                right_subtree_height = 2**right_subtree_height - 1
                return 1 + right_subtree_height + count_inclusive_nodes(node.left)

        return count_inclusive_nodes(root)

    def countNodes_not_working(self, root: Optional[TreeNode]) -> int:
        def get_height(node: Optional[TreeNode], height: int = 0):
            if not node:
                return height
            return get_height(node.left, height + 1)

        tree_height = get_height(root)

        def is_the_last_node_in_the_right_subtree(
            node: Optional[TreeNode], height: int
        ) -> bool:
            node = node.right
            height += 1

            while node:
                node = node.left
                height += 1

            return height == tree_height

        def find_the_leftmost_node(node: Optional[TreeNode]):
            current_level = 0
            lefts = []

            while node and node.left:
                if is_the_last_node_in_the_right_subtree(node, current_level):
                    node = node.right
                    lefts.append(False)
                else:
                    node = node.left
                    lefts.append(True)

                current_level += 1

            return lefts

        def get_last_level_count() -> int:
            raise "IDK"

        count_of_nodes_without_last_level = 2 ** (tree_height - 1) - 1
        last_level_count = get_last_level_count()

        return count_of_nodes_without_last_level + last_level_count


if __name__ == "__main__":

    def build_tree(values: list[int], index: int = 0) -> Optional[TreeNode]:
        if index >= len(values):
            return None

        if values[index] is None:
            return None

        return TreeNode(
            values[index],
            build_tree(values, 2 * index + 1),
            build_tree(values, 2 * index + 2),
        )

    def test(values: list[int], expected: int):
        tree = build_tree(values)
        result = Solution().countNodes(tree)
        assert result == expected, f"{result=}, {expected=}"

    test([1, 2, 3, 4, 5, 6], 6)
    test([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
