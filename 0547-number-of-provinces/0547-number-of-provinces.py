class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Initialise adj list
        n = len(isConnected)
        adj ={i:[] for i in range(n)}
        for u in range(n):
            for v in range(n):
                if isConnected[u][v]==1:
                    adj[u].append(v)
                    adj[v].append(u)
        # ===> O(n^2)
        
        def dfs(node):
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited: dfs(neigh)

        count = 0
        visited = set()
        for i in range(n):
            # if i not in visited, do dfs and count+=1
            if i not in visited:
                dfs(i)
                count+=1
        return count


