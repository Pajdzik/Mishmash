#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-linked-list-cycle

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    visited = set()
    node = head
    
    while node != None:
        if node in visited:
            return 1

        visited.add(node)
        node = node.next

    return 0