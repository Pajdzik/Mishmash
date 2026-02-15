#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def init_queue(self, root: Optional[TreeNode]):
        order = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)
            order.append(node.val)
            inorder(node.right)

        inorder(root)
        return order

    def __init__(self, root: Optional[TreeNode]):
        self.queue = self.init_queue(root)
        self.index = -1

    def next(self) -> int:
        self.index += 1
        return self.queue[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.queue)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == "__main__":
    root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    iter = BSTIterator(root)
    assert iter.next() == 3
