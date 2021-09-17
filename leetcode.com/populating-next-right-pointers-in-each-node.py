#!/bin/python3
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from tkinter.tix import Tree


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
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

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
Solution().connect(root)