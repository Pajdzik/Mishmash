#!/bin/python3

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        if m <= 0:
            return 0

        prohibited_transitions = [ [ 0 for _ in range(10) ] for _ in range(10) ]
        prohibited_transitions[1][3] = prohibited_transitions[3][1] = 2
        prohibited_transitions[1][7] = prohibited_transitions[7][1] = 4

        prohibited_transitions[1][9] = prohibited_transitions[9][1] = 5
        prohibited_transitions[2][8] = prohibited_transitions[8][2] = 5
        prohibited_transitions[3][7] = prohibited_transitions[7][3] = 5
        prohibited_transitions[4][6] = prohibited_transitions[6][4] = 5

        prohibited_transitions[3][9] = prohibited_transitions[9][3] = 6
        prohibited_transitions[7][9] = prohibited_transitions[9][7] = 8

        count = 0

        def find_all_combinations(last_digit: int, length: int, visited: list[bool]) -> None:
            nonlocal count
            if length > n:
                return

            for i in range(1, 10):
                if i == last_digit:
                    continue

                if visited[i]:
                    continue

                j = prohibited_transitions[last_digit][i]

                if j == 0 or j > 0 and visited[j]:
                    if length >= m:
                        count += 1
                    visited[i] = True
                    find_all_combinations(i, length + 1, visited)
                    visited[i] = False


        visited = [ False ] * 10
        find_all_combinations(0, 1, visited)
        return count

if __name__ == "__main__":
    assert(Solution().numberOfPatterns(1, 3) == 385)
    assert(Solution().numberOfPatterns(1, 2) == 65)