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
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1":
                    bfs(row, col)
                    count+=1
        return count