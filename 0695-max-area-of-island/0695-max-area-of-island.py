class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m,n = len(grid), len(grid[0])

        def dfs(r, c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]==0: return 0
            grid[r][c] = 0
            area = 1
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            return area
            
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        return max_area