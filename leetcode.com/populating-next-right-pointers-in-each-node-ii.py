#!/bin/python3
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        queue = [ root ]

        while True:
            level = []

            while len(queue) > 0:
                node = queue.pop(0)

                if node.left:
                    level.append(node.left)
                
                if node.right:
                    level.append(node.right)

            for i in range(0, len(level) - 1):
                level[i].next = level[i + 1]

            queue = level
            if len(queue) == 0:
                break

        return root