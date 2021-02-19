#!/usr/bin/env python

class StackNode:
    def __init__(self, value):
        self.next = None
        self.value = value

class Stack:
    def __init__(self):
        self.top = None

    def push(self, element):
        node = StackNode(element)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None

        value = self.top.value
        self.top = self.top.next

        return value

    def peek(self):
        return self.top.value

    def empty(self):
        return self.top is None

    def print(self, end="\n"):
        node = self.top

        while node is not None:
            print(node.value, end=", ")
            node = node.next

        print(end=end)

if __name__ == "__main__":
    stack = Stack()

    stack.push(6)
    stack.print()
    stack.push(2)
    stack.print()
    stack.push(4)
    stack.print()
    print("pop: {}".format(stack.pop()))
    stack.print()
    stack.push(9)
    stack.print()
    print("pop: {}".format(stack.pop()))
    stack.print()
    print("pop: {}".format(stack.pop()))
    stack.print()
    print("pop: {}".format(stack.pop()))
    stack.print()
    print("pop: {}".format(stack.pop()))

