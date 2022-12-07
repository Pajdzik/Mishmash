#!/usr/bin/env python3
# https://adventofcode.com/2022/day/6

import io
from collections import Counter

def find_marker(file: io.TextIOWrapper) -> int:
    input = file.readline()
    last_four = list(input[0:4])
    counter = Counter(last_four)

    for i in range(4, len(input)):
        c = input[i]
        if len(counter) == 4:
            return i
        
        last_letter = last_four[i % 4]
        last_char = counter[last_letter]

        if last_char == 1:
            del counter[last_letter]
        else:
            counter[last_letter] -= 1

        last_four[i % 4] = c
        counter[c] += 1

        

if __name__ == "__main__":
    input = open("day6.txt", "r")
    result = find_marker(input)
    print(result)
    input.close()