class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxarea = 0
        def dfs(r, c):
            if r<0 or r>=m or c<0 or r>=n or grid[r][c]!=1: return 0
            grid[r][c]=2
            area = 1
            area += dfs(r, c+1)
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c-1)
            return area
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1: maxarea = max(maxarea, dfs(r, c))
        return maxarea
         