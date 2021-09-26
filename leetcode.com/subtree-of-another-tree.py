#!/bin/python3
# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def compare(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue1 = [ root ]
        queue2 = [ subRoot ]

        while queue2:
            node1 = queue1.pop()
            node2 = queue2.pop()

            if node1 == node2 == None:
                continue
            if (not node1 and node2) or (node1 and not node2):
                return False
            if node1.val != node2.val:
                return False
            
            queue1.append(node1.left)
            queue2.append(node2.left)
            queue1.append(node1.right)
            queue2.append(node2.right)

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [ root ]

        while queue:
            node = queue.pop()
            if not node:
                continue

            if node.val == subRoot.val:
                result = self.compare(node, subRoot)
                if result:
                    return True

            queue.append(node.left)
            queue.append(node.right)

        return False