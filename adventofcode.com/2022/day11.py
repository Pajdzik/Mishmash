#!/usr/bin/env python3
# https://adventofcode.com/2022/day/11

from io import TextIOWrapper
from typing import Union

class Monkey:
    def __init__(self, config: list[str]) -> None:
        self.id = self.parse_id(config[0])
        self.items = self.parse_starting_items(config[1])
        self.operation = self.parse_operation(config[2])
        self.test_divisor = self.parse_test(config[3])
        self.target = self.parse_target(config[4:])
        self.inspect_count = 0

    def parse_id(self, text: str) -> int:
        id = text.split(" ")[1].strip()[:-1]
        return int(id)
    
    def parse_starting_items(self, text: str) -> list[int]:
        starting_items_str = text.split(":")[1].strip()
        starting_items = [int(d.strip()) for d in starting_items_str.split(",")]
        return starting_items
    
    def parse_operation(self, text: str):
        operation_str = text.split(":")[1].strip()
        calculation_str = operation_str.split("=")[1].strip()
        lambda_str = [int(x) if x.isnumeric() else x for x in calculation_str.split(" ")]
        value1, operator, value2 = lambda_str

        return self.create_lambda(operator, value1, value2)

    def create_lambda(self, operator: str, value1: Union[str, int], value2: Union[str, int]):
        num_or_str_value, _ = (value1, value2) if type(value1) == int else (value2, value1)
        if operator == "+":
            if type(value1) == type(value2) == str:
                return lambda x: x + x
            else:
                return lambda x: x + num_or_str_value
        else:
            if type(value1) == type(value2) == str:
                return lambda x: x * x
            else:
                return lambda x: x * num_or_str_value

    def parse_test(self, text: str) -> int:
        divisible_by = text.split(":")[1].strip()
        divisor = int(divisible_by.split(" ")[2].strip())

        return divisor
    
    def parse_target(self, text: list[str]) -> tuple[int, int]:
        throw_tos = [x.split(":")[1].strip() for x in text]
        monkey_ids = [int(x.split(" ")[3]) for x in throw_tos]

        return monkey_ids[1], monkey_ids[0]

def load_monkeys(input: TextIOWrapper) -> tuple[dict[int, Monkey], int]:
    line = '\n'
    monkeys = {}
    truncator = 1

    while line:
        monkey_input = [input.readline() for _ in range(6)]
        if not monkey_input[-1]:
            break

        monkey = Monkey(monkey_input)
        monkeys[monkey.id] = monkey
        line = input.readline()

        truncator *= monkey.test_divisor

    return monkeys, truncator

def calculate_monkey_business(input: TextIOWrapper, part: int) -> int:
    monkeys, truncator = load_monkeys(input)

    for _ in range((20 if part == 1 else 10000)):
        for id in range(len(monkeys)):
            monkey = monkeys[id]
            items_count = len(monkey.items)

            for _ in range(items_count):
                monkey.inspect_count += 1

                worry_level = monkey.items.pop(0)
                new_worry_level = monkey.operation(worry_level) // (3 if part == 1 else 1)
                test_outcome = (new_worry_level % monkey.test_divisor) == 0
                target_monkey = monkey.target[int(test_outcome)]

                truncated_worry_level = new_worry_level % truncator
                monkeys[target_monkey].items.append(truncated_worry_level)

    inspect_counts = [m.inspect_count for m in monkeys.values()]
    inspect_counts.sort(reverse=True)

    return inspect_counts[0] * inspect_counts[1]
        
if __name__ == "__main__":
    input = open("day11.txt", "r")
    result_part1 = calculate_monkey_business(input, 1)
    print(f'Part 1: {result_part1}')
    input.close()

    input = open("day11.txt", "r")
    result_part2 = calculate_monkey_business(input, 2)
    print(f'Part 2: {result_part2}')
    input.close()