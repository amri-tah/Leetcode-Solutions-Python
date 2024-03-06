class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max Heap
        distances = []
    
        for x,y in points:
            # Tuple Comparision
            distances.append((- x**2 - y**2, [x, y]))
            
        heapq.heapify(distances)
        
        # Heap pop max values till only k values
        while len(distances)>k:
            heapq.heappop(distances)
            
        return [distances[i][1] for i in range(len(distances))]