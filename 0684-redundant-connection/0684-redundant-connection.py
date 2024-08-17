class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]

        def find(n1):
            if parent[n1]!=n1:
                parent[n1] = find(parent[n1])
            return parent[n1]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2: return False
            else:
                if rank[p1]>rank[p2]:
                    parent[p2] = p1
                elif rank[p2]>rank[p1]:
                    parent[p1] = p2
                else:
                    parent[p2] = p1
                    rank[p1] += 1
            return True
        
        for u, v in edges:
            if not union(u,v):
                return [u, v]
        