#!/bin/python3
# https://leetcode.com/problems/shuffle-an-array/

import random

class Solution:
    def __init__(self, nums: list[int]):
        self.size = len(nums)
        self.original_nums = nums

    def reset(self) -> list[int]:
        return self.original_nums

    def shuffle(self) -> List[int]:
        taken = [ False ] *  self.size
        result = [ None ] *  self.size

        for i in range(len(result)):
            random_index = self.__get_random_index()
            while taken[random_index]:
                random_index = self.__get_random_index()

            result[i] = self.original_nums[random_index]
            taken[random_index] = True

        return result

    def __get_random_index(self) -> int:
        return random.randrange(0, self.size)
