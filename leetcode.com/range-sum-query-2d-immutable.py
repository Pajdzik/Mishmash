from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.cache = self.init_cache(matrix)

    def init_cache(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]

        sum_r = sum_c = cache[0][0] = matrix[0][0]

        for r in range(1, m):
            sum_r += matrix[r][0]
            cache[r][0] = sum_r

        for c in range(1, n):
            sum_c += matrix[0][c]
            cache[0][c] = sum_c

        for r in range(1, m):
            for c in range(1 ,n):
                cache[r][c] = cache[r -  1][c] + cache[r][c - 1] - cache[r - 1][c - 1] + matrix[r][c]

        return cache
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        full_square = self.cache[row2][col2]
        small_square = self.cache[row1 - 1][col1 - 1] if col1 > 0 and row1 > 0 else 0
        left_square = self.cache[row2][col1 - 1] if col1 > 0 else 0
        top_square = self.cache[row1 - 1][col2] if row1 > 0 else 0

        return full_square - left_square - top_square + small_square
        
if __name__ == "__main__":
    matrix = NumMatrix([[-4, -5]])
    sum_region = matrix.sumRegion(0, 0, 0, 1)
    assert(sum_region == -5)

    matrix = NumMatrix([[-1]])
    sum_region = matrix.sumRegion(0, 0, 0, 0)
    assert(sum_region == -1)