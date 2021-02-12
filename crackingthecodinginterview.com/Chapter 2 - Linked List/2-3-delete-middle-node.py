#!/usr/bin/env python
# Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not necessarily the exact middle) 
# of a singly linked list, given only access to that node.

from linkedlist import new_linked_list, print_linked_list

def delete_middle_node(middle_node):
    if middle_node is None:
        return

    if middle_node.next:
        middle_node.value = middle_node.next.value
        middle_node.next = middle_node.next and middle_node.next.next

def run_and_print(root_node, k):
    print_linked_list(root_node)
    middle_node = root_node.next.next
    delete_middle_node(middle_node)
    print_linked_list(root_node)
    print("")

if __name__ == "__main__":
    input_root = new_linked_list([1, 2, 3, 4])
    run_and_print(input_root, 1)

    input_root = new_linked_list([1, 1, 3, 1])
    run_and_print(input_root, 2)
    
    input_root = new_linked_list([1, 1, 3, 1])
    run_and_print(input_root, 3)

    input_root = new_linked_list([1, 1, 3, 1])
    run_and_print(input_root, 6)
