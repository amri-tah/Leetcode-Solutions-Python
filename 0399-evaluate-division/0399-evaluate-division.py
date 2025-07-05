class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(start, end, visited):
            if start not in adj or end not in adj: return -1.0
            if start == end: return 1.0
            visited.add(start)
            for neighbor, weight in adj[start]:
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0: return res * weight
            return -1.0
        adj = defaultdict(list)
        result = []
        for edge, val in zip(equations, values):
            u, v = edge
            adj[u].append([v, val])
            adj[v].append([u, 1/val])
        for start, end in queries:
            result.append(dfs(start,end, set()))
        return result