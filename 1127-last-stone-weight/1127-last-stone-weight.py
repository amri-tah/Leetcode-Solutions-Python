class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1 = abs(heapq.heappop(stones))
            stone2 = abs(heapq.heappop(stones))
            if stone1==stone2: continue
            else: heapq.heappush(stones, -(stone1-stone2))
        return 0 if not stones else abs(stones[0])
            
