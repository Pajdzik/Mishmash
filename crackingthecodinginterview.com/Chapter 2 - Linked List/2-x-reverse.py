#!/usr/bin/env python
# Reverse a linked list

from linkedlist import new_linked_list, print_linked_list

def reverse_three_pointers(root_node):
    prev_node = None
    curr_node = root_node
    next_node = curr_node.next

    while next_node:
        curr_node.next = prev_node

        prev_node = curr_node
        curr_node = next_node
        next_node = next_node.next

    curr_node.next = prev_node
    return curr_node

def reverse(node, prev=None):
    if node.next is None:
        node.next = prev
        return node

    next_node = node.next
    node.next = prev
    return reverse(next_node, node)


def run_and_print(root_node):
    print_linked_list(root_node)
    result_root = reverse(root_node)
    print_linked_list(result_root)
    print("")

if __name__ == "__main__":
    input_root = new_linked_list([1, 2, 3, 4])
    run_and_print(input_root)

    input_root = new_linked_list([1, 1, 3, 1])
    run_and_print(input_root)

    input_root = new_linked_list([1, 1, 1])
    run_and_print(input_root)

    input_root = new_linked_list([1, 2, 1, 1])
    run_and_print(input_root)

    input_root = new_linked_list([1, 2, 2, 1])
    run_and_print(input_root)
