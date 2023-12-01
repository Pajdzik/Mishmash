#!/usr/bin/env python3
# https://adventofcode.com/2022/day/2

OP_ROCK = 'A'
OP_PAPER = 'B'
OP_SCISSORS = 'C'

PL_ROCK = 'X'
PL_PAPER = 'Y'
PL_SCISSORS = 'Z'

LOSS = 'X'
DRAW = 'Y'
WIN = 'Z'

MOVE_SCORES = {
    PL_ROCK: 1,
    PL_PAPER: 2,
    PL_SCISSORS: 3
}

DRAWS = {
    OP_PAPER: PL_PAPER,
    OP_ROCK: PL_ROCK,
    OP_SCISSORS: PL_SCISSORS
}

LOSSES = {
    OP_PAPER: PL_ROCK,
    OP_ROCK: PL_SCISSORS,
    OP_SCISSORS: PL_PAPER
}

WINS = {
    OP_PAPER: PL_SCISSORS,
    OP_ROCK: PL_PAPER,
    OP_SCISSORS: PL_ROCK
}

OUTCOMES = {
    LOSS: LOSSES,
    DRAW: DRAWS,
    WIN: WINS
}

SCORES = {
    DRAW: 3,
    LOSS: 0,
    WIN: 6,
}

def outcome_part1(op_move: str, pl_move: str) -> int:
    score = 0
    if op_move == OP_ROCK and pl_move == PL_ROCK \
        or op_move == OP_PAPER and pl_move == PL_PAPER \
        or op_move == OP_SCISSORS and pl_move == PL_SCISSORS:
        score = 3
    elif op_move == OP_ROCK and pl_move == PL_PAPER \
        or op_move == OP_PAPER and pl_move == PL_SCISSORS \
        or op_move == OP_SCISSORS and pl_move == PL_ROCK:
        score = 6
    else:
        score = 0

    return score + MOVE_SCORES[pl_move]

def outcome_part2(op_move: str, outcome: str) -> int:
    move = OUTCOMES[outcome][op_move]
    move_score = MOVE_SCORES[move]
    score = SCORES[outcome]

    return score + move_score

def count_score(input, outcome) -> int:
    score = 0
    for line in input:
        opponent_move, player_move = line.split()
        score += outcome(opponent_move, player_move)
    
    return score
        
if __name__ == "__main__":
    input = open('day2.txt', 'r')
    score_part1 = count_score(input, outcome_part1)
    print(f'Part 1: {score_part1}')
    input.close()

    input = open('day2.txt', 'r')
    score_part2 = count_score(input, outcome_part2)
    print(f'Part 2: {score_part2}')
    input.close()
