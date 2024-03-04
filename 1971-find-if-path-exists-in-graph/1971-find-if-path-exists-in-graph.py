class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(source):
            if source==destination:
                return True
            
            visited.add(source)     
            
            for neighbour in edges_dict[source]:
                if neighbour not in visited and dfs(neighbour):
                    return True
                
            return False
        
        visited = set()
        
        # Create adj list
        edges_dict = defaultdict(list)
        for [u, v] in edges:
            edges_dict[u].append(v)
            edges_dict[v].append(u)
            
        return dfs(source)
    
    
            
            