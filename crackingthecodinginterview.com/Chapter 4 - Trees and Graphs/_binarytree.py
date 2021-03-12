#!/usr/bin/env python

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add_node(node, value):
    if (value < node.value):
        if node.left is None:
            node.left = Node(value)
        else:
            add_node(node.left, value)
    else:
        if node.right is None:
            node.right = Node(value)
        else:
            add_node(node.right, value)


def create_binary_tree(nodes):
    root_node = Node(nodes[0])

    for node in nodes[1:]:
        add_node(root_node, node)

    return root_node

def get_height(root):
    height = 0
    node = root

    while node:
        height += 1
        node = node.left

    return height + 1

def print_binary_tree(root):
    levels = []
    levels.append([root])

    while True:
        level = []
        for node in levels[-1]:
            if node is None:
                level.append(None)
                level.append(None)
            else:
                level.append(node.left)
                level.append(node.right)

        if any(map(lambda n: n != None, level)):
            levels.append(level)
        else:
            break

    width = len(levels[-1]) * 2

    for level in levels:
        for node in level:
            print(str("  " * width), end='')
            print(str((node and node.value) or "_"), end='')

        width = (width // 2)
        print()
        print()

if __name__ == "__main__":
    root = create_binary_tree([5, 2, 8, 1, 3, 6, 9])
    print_binary_tree(root)

    root = create_binary_tree([5, 6, 8, 9, 3, 10, 9])
    print_binary_tree(root)

