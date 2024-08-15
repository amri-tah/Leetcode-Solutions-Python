class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i:[] for i in range(1,n+1)}
        for u,v,w in times:
            edges[u].append((w, v))
        frontier = [[0, k]]
        visited = set()
        min_time = 0

        while frontier:
            w, v = heapq.heappop(frontier)
            if v in visited: continue
            visited.add(v)
            min_time = max(min_time, w)
            for weight, neigh in edges[v]:
                if neigh not in visited: heapq.heappush(frontier, (weight+w, neigh))
        
        if len(visited)==n: return min_time
        else: return -1
