class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-weight for weight in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            y = abs(heapq.heappop(maxHeap))
            x = abs(heapq.heappop(maxHeap))
            if x!=y: heapq.heappush(maxHeap, -(y-x)) 
        if not maxHeap: return 0
        else: return abs(maxHeap[0])