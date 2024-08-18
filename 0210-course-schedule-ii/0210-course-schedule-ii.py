class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        result = []
        graph = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = deque([i for i in range(numCourses) if indegree[i]==0])
        while queue:
            course = queue.popleft()
            result.append(course)
            for prereq in graph[course]:
                indegree[prereq]-=1
                if indegree[prereq]==0: queue.append(prereq)
        if len(result)!=numCourses: return []
        return result