class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
        
        visited = set()
        def dfs(node):
            if node in visited: return False # Loop in the graph
            if len(adj[node])==0: return True # Finish-able task

            visited.add(node)
            for neigh in adj[node]:
                if not dfs(neigh): return False
                    
            visited.remove(node)
            adj[node] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True