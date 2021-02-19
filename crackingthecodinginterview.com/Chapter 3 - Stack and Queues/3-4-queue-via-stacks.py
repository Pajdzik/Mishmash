#!/usr/bin/env python
# Implement a MyQueue class which implements a queue using two stacks.

from _stack import Stack

class TwoStacksQueue:
    def __init__(self):
        self.old = Stack()
        self.new = Stack()

    def enqueue(self, element):
        self.new.push(element)

    def dequeue(self):
        self.__inverse_stacks()
        return self.old.pop()

    def peek(self):
        self.__inverse_stacks()
        return self.old.peek()

    def print(self):
        print("NEW: {", end="")
        self.new.print(end="")
        print("}")

        print("OLD: {", end="")
        self.old.print(end="")
        print("}")

    def __inverse_stacks(self):
        if self.old.empty():
            while not self.new.empty():
                self.old.push(self.new.pop())

if __name__ == "__main__":
    queue = TwoStacksQueue()
    queue.enqueue(1)
    queue.print()
    queue.enqueue(3)
    queue.print()
    print("EL: {}".format(queue.dequeue()))
    queue.print()
    queue.enqueue(5)
    queue.print()
    print("EL: {}".format(queue.dequeue()))
    queue.print()
    print("EL: {}".format(queue.dequeue()))
    queue.print()