from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        sets = [-1] * n  # -1 if not assigned, 1 if in set 1, 2 if in set 2

        def bfs(start):
            queue = deque()
            queue.append((start, 1))
            
            while queue:
                node, color = queue.popleft()
                for neigh in graph[node]:
                    if sets[neigh] == -1:  
                        sets[neigh] = 2 if color == 1 else 1
                        queue.append((neigh, sets[neigh]))
                    elif sets[neigh] == color: return False
            return True

        for start in range(n):
            if sets[start] == -1: 
                if not bfs(start):
                    return False
        return True
