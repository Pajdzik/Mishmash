#!/usr/bin/env python
# Write code to remove duplicates from an unsorted list

from linkedlist import new_linked_list, print_linked_list

def remove_dups_with_buffer(root_node):
    visited = { root_node.value }
    prev_node = root_node
    curr_node = root_node.next
    
    while curr_node:
        if curr_node.value in visited:
            prev_node.next = curr_node.next
        else:
            visited.add(curr_node.value)
            prev_node = curr_node

        curr_node = curr_node.next

    return root_node

def remove_dups(root_node):
    outer_node = root_node
    
    while outer_node:
        prev_node = outer_node
        inner_node = outer_node.next

        while inner_node:
            if outer_node.value == inner_node.value:
                prev_node.next = inner_node.next
            else:
                prev_node = inner_node
                
            inner_node = inner_node.next

        outer_node = outer_node.next

    return root_node

def run_and_print(root_node):
    print_linked_list(root_node)
    result_root = remove_dups(root_node)
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
