#!/bin/python3
# https://leetcode.com/problems/same-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = [ p ]
        queue_q = [ q ]

        while len(queue_p) > 0 and len(queue_q) > 0:
            p_node = queue_p.pop()
            q_node = queue_q.pop()

            if p_node == None or q_node == None:
                if p_node == None and q_node == None:
                    continue
                else:
                    return False

            if p_node.val != q_node.val:
                return False

            queue_p.append(p_node.left)
            queue_q.append(q_node.left)
            queue_p.append(p_node.right)
            queue_q.append(q_node.right)
            
        return len(queue_q) == len(queue_p) == 0

