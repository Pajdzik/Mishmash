#!/usr/bin/env python
# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time. 

class MinStack:
    def __init__(self):
        self.__min_index = -1
        self.__index = -1
        self.__array = []

    def pop(self):
        if self.__index <= 0:
            return None

        index = self.__index
        element = self.__array[index]
        del self.__array[index]

        if self.__min_index == index:
            min_index = 0
            for i in range(self.__index):
                if self.__array[min_index] > self.__array[i]:
                    min_index = i

            self.__min_index = min_index

        self.__index -= 1
        return element


    def push(self, element):
        self.__index += 1

        if len(self.__array) <= self.__index:
            self.__array.extend([0]*8)
        
        if self.__index == 0 or element < self.__array[self.__min_index]:
            self.__min_index = self.__index

        self.__array[self.__index] = element

    def peek(self):
        return self.__array[self.__index]

    def min(self):
        if self.__min_index == -1:
            return None
        return self.__array[self.__min_index]

    def print(self):
        for i in range(self.__index + 1):
            print(self.__array[i], end=", ")

        print("[min: {}]".format(self.__array[self.__min_index]))


if __name__ == "__main__":
    stack = MinStack()

    stack.push(4)
    stack.print()
    stack.push(5)
    stack.print()
    stack.push(1)
    stack.print()
    stack.push(5)
    stack.print()
    stack.pop()
    stack.print()
    stack.pop()
    stack.print()
