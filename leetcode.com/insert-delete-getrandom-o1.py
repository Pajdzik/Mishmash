#!/bin/python3
# https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import Random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.top = -1
        self.numbers = [ ]
        self.positions = { }
        self.random = Random()
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.positions:
            self.top += 1
            self.numbers.append(val)
            self.positions[val] = self.top
            return True

        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.positions:
            last_element = self.numbers[self.top]
            val_index = self.positions[val]

            self.positions[last_element] = val_index
            self.numbers[val_index] = last_element
            self.numbers[self.top] = None

            self.numbers.pop()
            del self.positions[val]

            self.top -= 1

            return True

        return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_index = self.random.randint(0, self.top)
        return self.numbers[random_index]
        

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
results = []
res = obj.insert(0)
results.append(res)

res = obj.insert(1)
results.append(res)

res = obj.remove(0)
results.append(res)

res = obj.insert(2)
results.append(res)

res = obj.remove(1)
results.append(res)

res = obj.getRandom()
results.append(res)

pass