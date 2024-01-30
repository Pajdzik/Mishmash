# https://leetcode.com/problems/copy-list-with-random-pointer

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        def copy_node_with_value(node: Optional['Node'], node_map: dict) -> Optional['Node']:
            if not node:
                return None
            new_node = Node(node.val)
            node_map[node] = new_node
            return new_node

        dummy_new_head = Node(0)

        node_map = {}
        new_node = dummy_new_head

        node = head
        while node:
            new_node.next = copy_node_with_value(node, node_map)
            node = node.next
            new_node = new_node.next

        node = head
        while node:
            matching_new_node = node_map[node]
            if node.random and node.random in node_map:
                matching_new_node.random = node_map[node.random]
            elif node.random:
                matching_new_node.random = Node(node.random.val)

            node = node.next

        return dummy_new_head.next
