#!/bin/python3
# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorder_recursive(self, node: Optional[TreeNode], results: list[int]):
        if node == None:
            return
        if node.left == node.right == None:
            results.append(node.val)
            return

        if node and node.left:
            self.postorder_recursive(node.left, results)
        
        if node and node.right:
            self.postorder_recursive(node.right, results)

        results.append(node.val)


    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
            
        NEW = 0
        LEFT_DONE = 1
        RIGHT_DONE = 2

        result = []
        stack = [ [root, NEW] ]

        while stack:
            node, status = stack[-1]

            if status == RIGHT_DONE:
                stack.pop()
                result.append(node.val)
            else:
                next_node = None
                if status == NEW:
                    stack[-1][1] = LEFT_DONE
                    next_node = node.left
                elif status == LEFT_DONE:
                    stack[-1][1] = RIGHT_DONE
                    next_node = node.right

                if next_node:
                    stack.append([next_node, NEW])

        return result