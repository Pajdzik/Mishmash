#!/bin/python3
#https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list
import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data), end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    t_prev = None
    curr_node = head
    t_next = head.next

    while curr_node.next != None:
        t_next = curr_node.next
        t_prev = curr_node.prev

        curr_node.next = t_prev
        curr_node.prev = t_next

        curr_node = t_next

    curr_node.next = t_next.prev if t_next != None else None
    curr_node.prev = None
    return curr_node


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input", "reverse-a-doubly-linked-list.04.txt"), "r") as f:
        j = 0
        i = f.readlines()
        t = int(i[j])

        for t_itr in range(t):
            j == 1
            llist_count = int(i[j])

            llist = DoublyLinkedList()

            for _ in range(llist_count):
                j += 1
                llist_item = int(i[j])
                llist.insert_node(llist_item)

            llist1 = reverse(llist.head)
            print_doubly_linked_list(llist1, ' ')