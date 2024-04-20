class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count, m, n = 0, len(grid), len(grid[0])
        visited = set()
        
        def bfs(r, c):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            
            while queue:
                row, col = queue.popleft()
                for x, y in directions:
                    nx, ny = row+x, col+y
                    if 0<=nx<m and 0<=ny<n:
                        if grid[nx][ny]=="1" and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1" and (row, col) not in visited:
                    bfs(row, col)
                    count+=1
        return count