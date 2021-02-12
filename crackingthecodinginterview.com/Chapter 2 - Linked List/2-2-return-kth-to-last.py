#!/usr/bin/env python
# Implement an algorithm to find the kth to last element of a singly linked list.

from linkedlist import new_linked_list, print_linked_list

def get_length(node):
    length = 0

    while node:
        length += 1
        node = node.next

    return length

def return_kth_to_last_calc_length(node, k):
    length = get_length(node)
    n = length - k

    while node:
        if n == 1:
            return node.value

        n -= 1
        node = node.next

    return None

def return_kth_to_last(node, k, counter):
    if node is None:
        return None

    counter += 1
    result_node = return_kth_to_last(node.next, k, counter)

    if counter == k:
        return node

    return result_node

def run_and_print(root_node, k):
    print_linked_list(root_node)
    result = return_kth_to_last(root_node, k, 0)
    print("{}th to last element: {}".format(k, result and result.value))
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
