class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Create a min heap of size k
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        # Only pop if length minheap > k
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        
        # Min element is present in the zeroth index of heap
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)