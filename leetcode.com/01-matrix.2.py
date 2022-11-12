import math

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if mat[r][c] == 0:
                    continue
                up = mat[r - 1][c] if r - 1 >= 0 else math.inf
                left = mat[r][c - 1] if c - 1 >= 0 else math.inf
                mat[r][c] = min(up, left) + 1


        for r in range(len(mat) - 1, -1, -1):
            for c in range(len(mat[r]) - 1, -1, -1):
                if mat[r][c] == 0:
                    continue
                down = mat[r + 1][c] if r + 1 < len(mat) else math.inf
                right = mat[r][c + 1] if c + 1 < len(mat[r]) else math.inf
                mat[r][c] = min(min(down, right) + 1, mat[r][c])

        return mat

    def updateMatrix_bfs(self, mat: list[list[int]]) -> list[list[int]]:
        def fill(start_r: int, start_c: int):
            queue = [(start_r, start_c, 0)]

            while queue:
                (r, c, dist) = queue.pop(0)
                if not 0 <= r < len(mat):
                    continue
                if not 0 <= c < len(mat[r]):
                    continue
                if 0 <= mat[r][c] < dist:
                    continue

                mat[r][c] = dist

                for (dr, dc) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    queue.append((r + dr, c + dc, dist + 1))

        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if mat[r][c] != 0:
                    mat[r][c] = -1
        
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if mat[r][c] == 0:
                    fill(r, c)

        return mat
    
if __name__ == "__main__":
    # mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    result = Solution().updateMatrix(mat)
    print(result)