#!/usr/bin/env python3

def format_binary(number):
    return "{0:016b}".format(number)

def print_binary(number):
    print(format_binary(number))

def binary_array_to_number(binary):
    number = 0

    for i in range(0, len(binary)):
        n = int(binary[i])
        number += n * 2**(len(binary) - 1 - i)

    return number

if __name__ == "__main__":
    m = binary_array_to_number("01010")
    print(m)
    print_binary(m)
    pass