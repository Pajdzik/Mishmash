#!/bin/python3
# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min == None or self.min >= val:
            self.min = val
            self.mins.append(val)
        
    def pop(self) -> None:
        val = self.stack.pop()

        if len(self.stack) == 0:
            self.min = None
        elif val == self.min:
            self.mins.pop()
            self.min = self.mins[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
minStack = MinStack();
minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)
val1 = minStack.top()
minStack.pop()
val2 = minStack.getMin()
minStack.pop()
val3 = minStack.getMin()
minStack.pop()
minStack.push(2147483647)
val4 = minStack.top()
minStack.getMin()
minStack.push(-2147483648)
val5 = minStack.top()
val6 = minStack.getMin()
minStack.pop()
val7 = minStack.getMin()
pass