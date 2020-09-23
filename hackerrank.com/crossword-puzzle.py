#!/bin/python3
#https://www.hackerrank.com/challenges/crossword-puzzle

import math
import os
import random
import re
import sys

def sanitize_input(crossword_input, words_input):
    crossword = [list(line) for line in crossword_input]

    words = words_input.split(";")
    words_length = { len(word): [] for word in words }
    for word in words:
        length = len(word)
        words_length[length] = [] if length not in words_length else words_length[length] + [word]

    return crossword, words_length

def find_longest_gap_length(crossword, column_index = None, row_index = None):
    max_length = 0
    length = 0
    max_x, max_y = None, None
    x, y = None, None
    consecutive = False
    has_placeholders = False

    for i in range(0, len(crossword)):
        element = None

        if column_index != None:
            element = crossword[i][column_index]
        else:
            element = crossword[row_index][i]

        is_last_element = (i + 1 == len(crossword))

        if not is_last_element and element not in ("+", "X"):
            if element == "-":
                has_placeholders = True

            if consecutive:
                length += 1
            else:
                length = 1
                x, y = (i, column_index) if column_index != None else (row_index, i)
                consecutive = True
        else:
            if is_last_element and element not in ("+", "X"):
                length += 1

            if max_length < length:
                max_length = length
                max_x, max_y = x, y

            consecutive = False
            length = 0

    if not has_placeholders:
        return 0, None, None

    return max_length, max_x, max_y

def fill_word(crossword, word, row_index, column_index, horizontal):
    start = column_index if horizontal else row_index
    
    for i in range(len(word)):
        if horizontal:
            crossword[row_index][start + i] = word[i]
        else:
            crossword[start + i][column_index] = word[i]

def get_pattern(crossword, length, row_index, column_index, horizontal):
    pattern = []
    start = column_index if horizontal else row_index
    for i in range(length):
        if horizontal:
            el = crossword[row_index][start + i]
        else:
            el = crossword[start + i][column_index]

        pattern.append(el)

    return pattern

def find_pattern_match(pattern, words_length):
    matches = []

    if len(pattern) not in words_length:
        return []

    words = words_length[len(pattern)]

    for word in words:
        match = True
        for i in range(len(pattern)):
            if pattern[i] != '-' and pattern[i] != word[i]:
                match = False
                break
        
        if match:
            matches.append(word)

    return matches

def remove_word(words_length, word):
    word_length = len(word)
    if len(words_length[word_length]) == 1:
        del words_length[word_length]
    else:
        words_length[word_length].remove(word)

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword_input, words_input):
    crossword, words_length = sanitize_input(crossword_input, words_input)
    
    while len(words_length) > 0:
        empty_iteration = True

        # fill rows with matching length
        for i in range(len(crossword)):
            gap_length, x, y = find_longest_gap_length(crossword, row_index=i)
            if gap_length > 1:
                if gap_length in words_length and len(words_length[gap_length]) == 1:
                    word = words_length[gap_length][0]
                    fill_word(crossword, word, x, y, horizontal=True)
                    remove_word(words_length, word)
                    empty_iteration = False

        # fill columns with matching length
        for j in range(len(crossword)):
            gap_length, x, y = find_longest_gap_length(crossword, column_index=j)
            if gap_length > 1:
                if gap_length in words_length and len(words_length[gap_length]) == 1:
                    word = words_length[gap_length][0]
                    fill_word(crossword, word, x, y, horizontal=False)
                    remove_word(words_length, word)
                    empty_iteration = False

        # check row matches
        for i in range(len(crossword)):
            gap_length, x, y = find_longest_gap_length(crossword, row_index=i)
            if gap_length > 1:
                pattern = get_pattern(crossword, gap_length, x, y, horizontal=True)
                matches = find_pattern_match(pattern, words_length)
                if len(matches) == 1:
                    fill_word(crossword, matches[0], x, y, horizontal=True)
                    remove_word(words_length, matches[0])
                    empty_iteration = False

        # and columns        
        for j in range(len(crossword)):
            gap_length, x, y = find_longest_gap_length(crossword, column_index=j)
            if gap_length > 1:
                pattern = get_pattern(crossword, gap_length, x, y, horizontal=False)
                matches = find_pattern_match(pattern, words_length)
                if len(matches) == 1:
                    fill_word(crossword, matches[0], x, y, horizontal=False)
                    remove_word(words_length, matches[0])
                    empty_iteration = False
                # a little hack
                if empty_iteration and len(matches) == 2:
                    if matches[0][0] == matches[1][-1]:
                        fill_word(crossword, matches[0], x, y, horizontal=False)
                        remove_word(words_length, matches[0])
                    else:
                        fill_word(crossword, matches[1], x, y, horizontal=False)
                        remove_word(words_length, matches[1])

    return [ ''.join(line) for line in crossword ]
    

if __name__ == '__main__':
    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()
    result = crosswordPuzzle(crossword, words)
    print('\n'.join(result))
