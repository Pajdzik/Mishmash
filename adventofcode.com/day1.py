#!/usr/bin/env python3
#https://adventofcode.com/2022/day/1

def find_max(input) -> int:
    max_sum = 0
    sum = 0

    for line in input:
        if line == "" or line == "\n":
            max_sum = max(max_sum, sum)
            sum = 0
        else:
            sum += int(line)

    return max_sum
                
if __name__ == '__main__':
    input = open('day1.txt', 'r')
    max = find_max(input)
    print(max)
    input.close()
