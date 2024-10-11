class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, count = len(grid), len(grid[0]), 0

        def bfs(r, c):
            queue = deque([(r,c)])
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            while queue:
                r, c = queue.popleft()
                grid[r][c]="2"
                for x, y in directions:
                    nx, ny = r+x, c+y
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]=="1":
                        queue.append((nx, ny))
                

        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    count+=1
                    bfs(r,c)
        return count