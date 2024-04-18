class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter, m, n = 0, len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    perimeter+=4
                    for x, y in directions:
                        nx, ny = row+x, col+y
                        if 0<=nx<m and 0<=ny<n:
                            if grid[nx][ny]==1: perimeter-=1
        
        return perimeter
                    