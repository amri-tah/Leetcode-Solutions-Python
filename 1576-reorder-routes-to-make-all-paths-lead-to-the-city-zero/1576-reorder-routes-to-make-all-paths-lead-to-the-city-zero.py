class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        orig_edges = set()
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
            orig_edges.add((u,v)) 
        reachable = [False] * n
        reachable[0] = True
        self.res = 0

        def dfs(node):
            for neighbor in adj[node]:
                if not reachable[neighbor]:
                    if (node, neighbor) in orig_edges: self.res += 1
                    reachable[neighbor] = True
                    dfs(neighbor)

        dfs(0)
        return self.res