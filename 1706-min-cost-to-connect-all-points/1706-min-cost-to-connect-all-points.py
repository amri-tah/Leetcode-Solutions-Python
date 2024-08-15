class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Initialize adj list, min heap and visited
        N = len(points)
        adj = {i:[] for i in range(N)}
        visited = set()
        frontier = [[0, 0]]
        min_cost = 0

        # Initialise adj along w cost of each edge
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        # ===> O(n^2)

        # Prims algo \U0001f57a
        while len(visited)!=N:
            cost, i = heapq.heappop(frontier)
            if i in visited: continue
            visited.add(i)
            min_cost+=cost
            for c, neigh in adj[i]:
                if neigh not in visited: heapq.heappush(frontier, (c, neigh))

        # ====> O(logn) = heap operations
        
        # Time complexity: O(n^2logn)
        return min_cost
