#!/bin/python3
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.stack = []
        self.is_reversed = False

    def push(self, x: int) -> None:
        if self.is_reversed:
            self.reverse()
        self.stack.append(x)

    def pop(self) -> int:
        if not self.is_reversed:
            self.reverse()

        return self.stack.pop() 

    def peek(self) -> int:
        index = -1 if self.is_reversed else 0
        return self.stack[index]

    def empty(self) -> bool:
        return len(self.stack) == 0

    def reverse(self) -> None:
        reverse_stack = []

        while self.stack:
            reverse_stack.append(self.stack.pop())

        self.is_reversed = not self.is_reversed
        self.stack = reverse_stack