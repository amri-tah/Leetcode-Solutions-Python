class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_effort = 0
        m, n = len(heights), len(heights[0])
        min_heap = [(0, 0, 0)] # (eff, x, y)
        Effort = [[float('inf')]*n for _ in range(m)]
        Effort[0][0] = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        while min_heap:
            curr_effort, x1, y1 = heapq.heappop(min_heap)
            if curr_effort>Effort[x1][y1]:continue
            for x, y in directions:
                nx, ny = x+x1, y+y1
                if 0<=nx<m and 0<=ny<n:
                    diff = max(curr_effort, abs(heights[nx][ny]-heights[x1][y1]))
                    if diff<Effort[nx][ny]: 
                        heapq.heappush(min_heap, (diff, nx, ny))
                        Effort[nx][ny] = diff
        return Effort[m-1][n-1]