#!/usr/bin/env python
#Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

def has_cycle(head):
    visited = set()
    node = head
    
    while node != None:
        if node in visited:
            return 1

        visited.add(node)
        node = node.next

    return 0