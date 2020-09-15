#!/bin/python3
#https://www.hackerrank.com/challenges/swap-nodes-algo

import os
import sys

def swap(indexes, node_index, depth, swap_level):
    if depth + 1 == swap_level:
        indexes[node_index][0], indexes[node_index][1] = indexes[node_index][1], indexes[node_index][0]

    swap(indexes, indexes[node_index][0], depth + 1, swap_level)
    swap(indexes, indexes[node_index][1], depth + 1, swap_level)

    # TODO

def traverse(indexes, node_index, result):
    if indexes[node_index][0] == -1:
        result.append(node_index)
    else:
        traverse(indexes, indexes[node_index][0], result)

    # TODO
    
def swapNodes(indexes, queries):
    queries = queries.sort(reverse=True)

    for query in queries:
        swap(indexes, 0, 1, query)
        
    return []

if __name__ == '__main__':
    n = int(input())
    indexes = []
    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
