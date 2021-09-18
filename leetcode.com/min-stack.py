#!/bin/python3
# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_queue = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        i = 0
        while i < len(self.min_queue) and val > self.min_queue[i]:
            i += 1
        self.min_queue.insert(i, val)
        
    def pop(self) -> None:
        val = self.stack.pop()
        i = 1
        for i in range(len(self.min_queue)):
            if self.min_queue[i] == val:
                break
        self.min_queue.pop(i)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_queue[0]
        
minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
val1 = minStack.getMin(); 
minStack.pop();
val2 = minStack.top();    
val3 = minStack.getMin();
pass