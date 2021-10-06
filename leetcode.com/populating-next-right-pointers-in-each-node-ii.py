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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = [ root ]
        while queue:
            level_len = len(queue)
            for i in range(0, level_len - 1):
                queue[i].next = queue[i + 1]

            while level_len > 0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_len -= 1

        return root

if __name__ == "__main__":
    Solution().connect(Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7))))