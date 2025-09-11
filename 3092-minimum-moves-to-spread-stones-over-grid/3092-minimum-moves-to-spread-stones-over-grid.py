class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def backtrack(i):
            if i==len(zeroes): return 0
            zerox, zeroy = zeroes[i]
            ans = float('inf')
            for extrax, extray in extras:
                if grid[extrax][extray]>1:
                    grid[extrax][extray]-=1
                    grid[zerox][zeroy]=1
                    ans = min(ans, abs(zerox - extrax) + abs(zeroy - extray) + backtrack(i + 1))
                    grid[extrax][extray]+=1
                    grid[zerox][zeroy]=0
            return ans

        zeroes, extras = [], []
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col]==0: zeroes.append((row, col))
                if grid[row][col]>1: extras.append((row, col))
        
        return backtrack(0)