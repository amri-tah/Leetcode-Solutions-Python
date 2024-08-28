class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            if r<0 or c<0 or r>=m or c>=n or grid2[r][c]!=1: return True
            if grid1[r][c]!=1: return False
            grid2[r][c]=0
            found = dfs(r+1, c) 
            found &= dfs(r-1, c) 
            found &= dfs(r, c+1) 
            found &= dfs(r, c-1)
            return found
        
        m, n = len(grid2), len(grid2[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if grid2[r][c]==1 and dfs(r,c): count+=1
                    
        return count