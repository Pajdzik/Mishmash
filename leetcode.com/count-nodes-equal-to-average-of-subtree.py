#!/bin/python3
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def foo(node: TreeNode) -> tuple[int, int, int]:
            if not node:
                return 0, 0, 0

            left_count, left_sum, left_result = foo(node.left)
            right_count, right_sum, right_result = foo(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            avg = total_sum // total_count
            result = 1 if avg == node.val else 0

            return total_count, total_sum, left_result + right_result + result

        _, _, result = foo(root)
        return result


if __name__ == "__main__":

    def test(expected: int, tree: list[int]):
        def tree_from_array(arr: list[int]) -> TreeNode:
            root = TreeNode(arr[0])
            nodes = [root]
            i = 1

            while i < len(arr):
                node = nodes.pop(0)

                if arr[i] is not None:
                    node.left = TreeNode(arr[i])
                    nodes.append(node.left)

                i += 1

                if i < len(arr) and arr[i] is not None:
                    node.right = TreeNode(arr[i])
                    nodes.append(node.right)

                i += 1

            return root

        root = tree_from_array(tree)
        result = Solution().averageOfSubtree(root)
        assert result == expected, f"{result} != {expected}"

    test(5, [4, 8, 5, 0, 1, None, 6])
