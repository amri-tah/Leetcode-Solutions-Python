class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        x1, x2, y1, y2 = n, 0, m, 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]==1:
                    x1 = min(x1, col)
                    x2 = max(x2, col)
                    y1 = min(y1, row)
                    y2 = max(y2, row)
        return (x2-x1+1)*(y2-y1+1)