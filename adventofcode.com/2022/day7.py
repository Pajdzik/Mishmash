#!/usr/bin/env python3
# https://adventofcode.com/2022/day/7

import io
from typing import Union

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name: str, parent_path: list[str]) -> None:
        self.name = name
        self.full_path = parent_path
        self.children: list[Union[Directory, File]] = []

def construct_tree(input: io.TextIOWrapper):
    root = Directory("/", [])
    stack = [root]

    while input:
        line = input.readline()
        if not line:
            break

        if line[0] == "$":
            command_line = line.split(" ")
            command = command_line[1].strip()

            if command == "cd":
                argument = command_line[2].strip()
                if argument == "/":
                    stack = [root]
                elif argument == "..":
                    stack.pop()
                else:
                    parent = stack[-1]
                    parent_path = [*parent.full_path, parent.name]
                    dir = Directory(argument, parent_path)
                    parent.children.append(dir)
                    stack.append(dir)
            elif command == "ls":
                output_pos = 0
                output_line = " "

                while True:
                    output_pos = input.tell()
                    output_line = input.readline().strip()
                    if not output_line or output_line[0] == "$":
                        input.seek(output_pos)
                        break

                    desc, name = output_line.split(" ")
                    if desc == "dir":
                        pass
                    else:
                        dir = stack[-1]
                        file = File(name, int(desc))
                        dir.children.append(file)

    return root

def calc_size(dir: Directory, dir_size_to_remove: int) -> tuple[int, int]:
    dir_size = 0

    for child in dir.children:
        if isinstance(child, File):
            dir_size += child.size
        else:
            child_dir_size, dir_size_to_remove = calc_size(child, dir_size_to_remove)
            dir_size += child_dir_size

    if dir_size <= 100000:
        dir_size_to_remove += dir_size

    return dir_size, dir_size_to_remove


def get_total_size(input: io.TextIOWrapper) -> int:
    tree = construct_tree(input)
    _, size_to_remove = calc_size(tree, 0)
    return size_to_remove

if __name__ == "__main__":
    input = open("day7.txt", "r")
    result = get_total_size(input)
    print(result)
    input.close()