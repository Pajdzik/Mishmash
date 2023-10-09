#!/bin/python3
# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = [[0 for _ in range(len(word1) + 1)]
               for _ in range(len(word2) + 1)]

        for i in range(len(mem[0])):
            mem[0][i] = i

        for i in range(len(mem)):
            mem[i][0] = i

        for r in range(1, len(mem)):
            for c in range(1, len(mem[r])):
                same_letter = word1[c - 1] == word2[r - 1]
                mem[r][c] = mem[r - 1][c - 1] if same_letter else min(mem[r - 1][c],
                                                                      mem[r][c - 1],
                                                                      mem[r - 1][c - 1]) + 1

        return mem[-1][-1]


if __name__ == "__main__":
    def test_and_print_failure(str1: str, str2: str, expected: int):
        result = Solution().minDistance(str1, str2)
        if result != expected:
            print(f'{str1} x {str2} expected {expected} got {result}')

    test_and_print_failure("zoologicoarchaeologist", "zoogeologist", 10)
    test_and_print_failure("intention", "execution", 5)
    test_and_print_failure("horse", "ros", 3)

'''
  _ h o r s e
_ 0 1 2 3 4 5
r 1 1 2 2 3 4  
o 2 2 1 2 3 4
s 3 3 2 2 2 3

'''


'''
horse
s

horse
os

horse
ros

horse
 ros

horse
  ros

horse
   ro

horse
    o
'''
