#!/usr/bin/env python3
# https://adventofcode.com/2022/day/12

from io import TextIOWrapper

HillMap = list[list[str]]
START = "S"
END = "E"

def parse_input(input: TextIOWrapper) -> HillMap:
    return [list(line.strip()) for line in input]


def find_point(hill_map: HillMap, type: str) -> tuple[int, int]:
    for r, row in enumerate(hill_map):
        for c, el in enumerate(row):
            if el == type:
                return r, c

    return -1, -1


def find_shortest_path(hill_map: HillMap, start_point: tuple[int, int], end_type: str, end_height: str) -> int:
    queue = [(*start_point, int(0))]
    visited = [[False for _ in range(len(hill_map[0]))]
               for _ in range(len(hill_map))]
    
    reverse = end_type == "a"

    while queue:
        r, c, dist = queue.pop(0)
        if hill_map[r][c] == end_type:
            return dist
        
        if visited[r][c]:
            continue
        else:
            visited[r][c] = True

        height = ord(hill_map[r][c])
        for delta_r, delta_c in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            new_r = r + delta_r
            new_c = c + delta_c

            if not 0 <= new_r < len(hill_map):
                continue
            if not 0 <= new_c < len(hill_map[new_r]):
                continue

            new_height_str = hill_map[new_r][new_c]
            new_height = ord(new_height_str if new_height_str != end_type else end_height) 

            if (reverse and new_height + 1 >= height) \
                or (not reverse and new_height <= height + 1):
                queue.append((new_r, new_c, dist + 1))

    return -1


def find_shortest_path_to_end(input: TextIOWrapper) -> int:
    hill_map = parse_input(input)
    start = find_point(hill_map, START)
    hill_map[start[0]][start[1]] = 'a'

    return find_shortest_path(hill_map, start, END, 'z')


def find_shortest_path_to_any_start(input: TextIOWrapper) -> int:
    hill_map = parse_input(input)
    start = find_point(hill_map, START)
    hill_map[start[0]][start[1]] = 'a'

    end = find_point(hill_map, END)
    hill_map[end[0]][end[1]] = 'z'

    return find_shortest_path(hill_map, end, 'a', 'a')


if __name__ == "__main__":
    input_path = f'{__file__.rstrip(".py")}.txt'

    input = open(input_path, "r")
    result_part1 = find_shortest_path_to_end(input)
    print(f'Part 1: {result_part1}')
    input.close()

    input = open(input_path, "r")
    result_part2 = find_shortest_path_to_any_start(input)
    print(f'Part 2: {result_part2}')
    input.close()
