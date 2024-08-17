class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ### Using DFS:
        # Initialise adj list
        n = len(isConnected)
        # adj ={i:[] for i in range(n)}
        # for u in range(n):
        #     for v in range(n):
        #         if isConnected[u][v]==1:
        #             adj[u].append(v)
        #             adj[v].append(u)
        # ===> O(n^2)
        
        # def dfs(node):
        #     visited.add(node)
        #     for neigh in adj[node]:
        #         if neigh not in visited: dfs(neigh)

        # count = 0
        # visited = set()
        # for i in range(n):
        #     # if i not in visited, do dfs and count+=1
        #     if i not in visited:
        #         dfs(i)
        #         count+=1
        # return count

        ### Using Union Find
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(n1):
            if parent[n1] != n1:
                parent[n1] = find(parent[n1])
            return parent[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2: return 0
            if rank[p1]>rank[p2]:
                parent[p2]=p1 # Set Parent of P2 as P1
            elif rank[p1]<rank[p2]:
                parent[p1]=p2 # Set Parent of P1 as P2
            else:
                parent[p2]=p1
                rank[p1]+=1
            return 1
        
        result=n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1: result -= union(i, j)
        return result
        




