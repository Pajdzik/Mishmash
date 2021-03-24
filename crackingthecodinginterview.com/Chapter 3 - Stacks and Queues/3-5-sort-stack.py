#!/usr/bin/env python
# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and isEmpty.

from _stack import Stack

class SortStack:
    def __init__(self):
        self.stack = Stack()

    def push(self, element):
        temp_stack = Stack()

        while not self.stack.empty() and element > self.stack.peek():
            temp_stack.push(self.stack.pop())

        self.stack.push(element)

        while not temp_stack.empty():
            self.stack.push(temp_stack.pop())

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def empty(self):
        return self.stack.empty()

    def print(self):
        self.stack.print()

if __name__ == "__main__":
    stack = SortStack()

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
    stack.print()
    stack.push(19)
    stack.print()
    stack.push(31)
    stack.print()
    print("pop: {}".format(stack.pop()))
    stack.print()
