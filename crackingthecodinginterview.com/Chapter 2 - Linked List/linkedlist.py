class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

def new_linked_list(elements):
    root_node = Node(elements[0])
    curr_node = root_node

    for idx in range(1, len(elements)):
        node = Node(elements[idx])
        curr_node.next = node
        curr_node = node

    return root_node
        
def print_linked_list(root_node):
    curr_node = root_node
    output = ""
    while curr_node:
        output += "{} -> ".format(curr_node.value)
        curr_node = curr_node.next

    print(output)