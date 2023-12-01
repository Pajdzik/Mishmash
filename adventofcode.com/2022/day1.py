#!/usr/bin/env python3
#https://adventofcode.com/2022/day/1

from io import TextIOWrapper

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

def find_three_maxes(input: TextIOWrapper):
    sums = []
    temp_sum = 0
    for line in input:
        if line == "" or line == "\n":
            sums.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(line)

    sums.sort(reverse=True)
    return sum(sums[:3])
                
if __name__ == '__main__':
    input = open('day1.txt', 'r')
    max = find_three_maxes(input)
    print(max)
    input.close()
