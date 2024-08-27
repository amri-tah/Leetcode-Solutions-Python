class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append([v, succProb[i]])
            graph[v].append([u, succProb[i]])
        
        visited = set()
        probability = [0]*n
        max_heap = []
        heapq.heapify(max_heap)
        for neigh, prob in graph[start_node]:
            heapq.heappush(max_heap, (-prob, neigh))
        visited.add(start_node)
        probability[start_node]=1

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            visited.add(node)
            probability[node] = max(probability[node], -prob)
            for neigh, next_prob in graph[node]:
                if neigh not in visited: heapq.heappush(max_heap, (prob*next_prob, neigh))
        return probability[end_node]