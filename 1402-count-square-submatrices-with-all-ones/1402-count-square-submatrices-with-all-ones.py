class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = {}
        def bfs(i, j):
            if (i, j) in cache: return cache[(i,j)]
            size = 1
            count = 0
            while i + size <= m and j + size <= n:
                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if matrix[x][y] == 0: return count   
                count += 1
                size += 1
            cache[(i, j)] = count
            return count

        total =0 
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==1:
                    total+=bfs(row, col)
        return total