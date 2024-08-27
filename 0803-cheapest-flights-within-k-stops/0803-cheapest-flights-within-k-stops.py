class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # (cost, current_city, stops)
        heap = [(0, src, 0)]
        dist = defaultdict(lambda: float('inf'))
        dist[(src, 0)] = 0
        
        while heap:
            cost, city, stops = heapq.heappop(heap)
            if city == dst: return cost
            
            if stops <= k:
                for neighbor, price in graph[city]:
                    new_cost = cost + price
                    if new_cost < dist[(neighbor, stops + 1)]:
                        dist[(neighbor, stops + 1)] = new_cost
                        heapq.heappush(heap, (new_cost, neighbor, stops + 1))
        
        return -1