class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        output = []
                    
        def dfs(node, path, output):
            if node==target:
                output.append(path)
            
            for nextNode in graph[node]:
                dfs(nextNode, path+[nextNode], output)
        
        dfs(0, [0], output)
        return output