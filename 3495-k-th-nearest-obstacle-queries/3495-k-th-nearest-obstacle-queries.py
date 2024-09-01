class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        results = []
        max_heap = []

        for x, y in queries:
            dist = abs(x)+abs(y)
            heapq.heappush(max_heap, -dist)
            if len(max_heap) > k: heapq.heappop(max_heap)
            if len(max_heap) >= k: results.append(-max_heap[0])
            else:results.append(-1)
        return results