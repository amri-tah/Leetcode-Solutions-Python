class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count, m, n = 0, len(grid), len(grid[0])
        
        def bfs(r, c):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "2"
            
            while queue:
                row, col = queue.popleft()
                for x, y in directions:
                    nx, ny = row+x, col+y
                    if 0<=nx<m and 0<=ny<n:
                        if grid[nx][ny]=="1" and grid[nx][ny]!="2":
                            queue.append((nx, ny))
                            grid[nx][ny]="2"

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n: return
            if grid[r][c]!="1":return
            else: grid[r][c]="2"
            dfs(r,c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1":
                    dfs(row, col)
                    count+=1
        return count