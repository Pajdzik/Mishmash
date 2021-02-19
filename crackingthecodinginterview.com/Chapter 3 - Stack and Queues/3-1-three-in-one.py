#!/usr/bin/env python
# Describe how you could use a single array to implement three stacks.  

class TripleStack:
    stack_count = 3

    def __init__(self):
        self.__index = [None, 1, 2, 3]
        self.__array = [None, None, None, None]

    def pop(self, stack_id):
        index = self.__index[stack_id]
        element = self.__array[index]
        self.__array[index] = None
        self.__index[stack_id] -= self.stack_count
        
        return element

    def push(self, stack_id, element):
        index = self.__index[stack_id] + self.stack_count
        if index >= len(self.__array):
            self.__array.extend([None, None, None])

        self.__array[self.__index[stack_id]] = element
        self.__index[stack_id] = index

    def peek(self, stack_id):
        index = self.__index[stack_id]
        element = self.__array[index]
        
        return element

    def print(self):
        for stack_id in range(1, self.stack_count + 1):
            print("Stack {}: ".format(stack_id), end="")
            self.print_single(stack_id)
            print();

    def print_single(self, stack_id):
        for _, el in filter(lambda t: t[0] < self.__index[stack_id] and t[0] % 3 == stack_id, enumerate(self.__array)):
            print(el, end=", ")

if __name__ == "__main__":
    stack = TripleStack()

    stack.push(1, 1)
    stack.push(2, 2)
    stack.push(2, 4)
    stack.push(2, 6)
    stack.push(2, 8)
    stack.print()
    stack.pop(2)
    stack.print()