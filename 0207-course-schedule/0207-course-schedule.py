class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        visited = set()
        def dfs(course):
            if course in visited: return False
            if not adj[course]: return True
            visited.add(course)
            for neigh in adj[course]:
                if not dfs(neigh):return False
            visited.remove(course)
            adj[course]=[]
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True