#!/bin/python3
# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack = [ ]
        result = [ ]
        curr = root

        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result

    def inorderTraversal_recursive(self, node: Optional[TreeNode], result: list[int]):
        if node == None:
            return 
        self.inorderTraversal_recursive(node.left, result)
        result.append(node.val)
        self.inorderTraversal_recursive(node.right, result)
        
Solution().inorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3)))