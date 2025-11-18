class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x==y: continue
            else: heapq.heappush(stones, y-x)
        if stones: return -stones[0]
        else: return 0