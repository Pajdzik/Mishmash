#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def split_index(start: int, end: int) -> int:
            val = preorder[start]
            i = start + 1
            while i < end and preorder[i] < val:
                i += 1

            return i

        def parse(start: int, end: int) -> Optional[TreeNode]:
            if start >= end or start >= len(preorder):
                return None

            val = preorder[start]
            split = split_index(start, end)
            node = TreeNode(val, parse(start + 1, split), parse(split, end))

            return node

        return parse(0, len(preorder))


if __name__ == "__main__":
    Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])
    pass
