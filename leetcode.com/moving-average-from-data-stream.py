#!/bin/python3
# https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.numbers = [ None for _ in range(size) ]
        self.index = 0
        self.sum = 0
        

    def next(self, val: int) -> float:
        index = self.index % self.size
        self.sum -= self.numbers[index] or 0
        self.numbers[index] = val
        self.sum += val
        self.index += 1
        
        return self.sum / min(self.size, self.index)