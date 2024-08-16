class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time, fresh = 0, 0
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        queue = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col]==1: fresh+=1
                if grid[row][col]==2: queue.append((row, col))
        
        while queue and fresh>0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for x, y in directions:
                    nx, ny = x+r, y+c
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh-=1
            time+=1
        
        return time if fresh==0 else -1