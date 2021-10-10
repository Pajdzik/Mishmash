#!/bin/python3
# https://leetcode.com/problems/closest-binary-search-tree-value/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff = float('inf')
        result = None
        queue = [ root ]
        
        while queue:
            node = queue.pop()
            if not node:
                continue

            diff = abs(node.val - target)
            
            if diff < min_diff:
                min_diff = diff
                result = node

            if target <= node.val:
                queue.append(node.left)
            else:
                queue.append(node.right)

        return result.val