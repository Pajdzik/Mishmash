#!/usr/bin/env python
# Implement an algorithm to find the kth to last element of a singly linked list.

from linkedlist import new_linked_list, print_linked_list

def return_kth_to_last(node, k):
    while node:
        if k == 1:
            return node.value

        k -= 1
        node = node.next

    return None

def run_and_print(root_node, k):
    print_linked_list(root_node)
    result = return_kth_to_last(root_node, k)
    print("{}th element: {}".format(k, result))
    print("")

if __name__ == "__main__":
    input_root = new_linked_list([1, 2, 3, 4])
    run_and_print(input_root, 1)

    input_root = new_linked_list([1, 1, 3, 1])
    run_and_print(input_root, 4)
    
    input_root = new_linked_list([1, 1, 3, 1])
    run_and_print(input_root, 3)

    input_root = new_linked_list([1, 1, 3, 1])
    run_and_print(input_root, 6)
