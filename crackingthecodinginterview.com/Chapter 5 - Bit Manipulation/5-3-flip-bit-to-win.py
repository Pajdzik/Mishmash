#!/usr/bin/env python3

# You have an integer and you can flip exactly one bit from a 0 to a 1,
# write code to find the length of the longest sequence of 1s you could create.

from _bit import print_binary

def find_sequences(n):
    current_value = 0
    current_length = 0
    sequences = []

    for bit in range(32, -1, -1):
        if (n & (1 << bit)) == (current_value << bit):
            current_length += 1
        else:
            sequences.append(current_length)
            current_value = 1 if current_value == 0 else 0
            current_length = 1

    return sequences

def flip_bit_to_win_with_additional_memory(n):
    sequences = find_sequences(n)
    max_length = 0

    for i in range(1, len(sequences), 2):
        if ((i + 1 < len(sequences)) and sequences[i + 1] == 1) \
          and ((i + 2 < len(sequences)) and sequences[i] + sequences[i + 2] > max_length):
            max_length = sequences[i] + sequences[i + 2]
        if sequences[i] > max_length:
            max_length = sequences[i]

    return max_length

def flip_bit_to_win(n):
    last_value = None
    current_value = 0
    max_length = 0
    previous_sequence = 0
    current_sequence = 0

    for bit in range(0, 33):
        if (n & (1 << bit)) == (1 << bit):
            current_sequence += 1
        else:


    return max_length

if __name__ == "__main__":
    n = 0xAE9B
    print_binary(n)
    print(flip_bit_to_win(n))
    pass