#!/usr/bin/env python3
# https://adventofcode.com/2022/day/2

OP_ROCK = 'A'
OP_PAPER = 'B'
OP_SCISSORS = 'C'

PL_ROCK = 'X'
PL_PAPER = 'Y'
PL_SCISSORS = 'Z'

MOVE_SCORES = {
    PL_ROCK: 1,
    PL_PAPER: 2,
    PL_SCISSORS: 3
}

def outcome(op_move: str, pl_move: str) -> int:
    if op_move == OP_ROCK and pl_move == PL_ROCK \
        or op_move == OP_PAPER and pl_move == PL_PAPER \
        or op_move == OP_SCISSORS and pl_move == PL_SCISSORS:
        return 3
    
    if op_move == OP_ROCK and pl_move == PL_PAPER \
        or op_move == OP_PAPER and pl_move == PL_SCISSORS \
        or op_move == OP_SCISSORS and pl_move == PL_ROCK:
        return 6

    return 0

def count_score(input) -> int:
    score = 0
    for line in input:
        opponent_move, player_move = line.split()
        score += outcome(opponent_move, player_move)
        score += MOVE_SCORES[player_move]
    
    return score
        
if __name__ == "__main__":
    input = open('day2.txt', 'r')
    score = count_score(input)
    print(score)
    input.close()
