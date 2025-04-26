class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        heap, output = [], []
        for num in nums:
            hash[num]+=1
        heap = [(-freq, val) for val, freq in hash.items()]
        heapq.heapify(heap)
        for _ in range(k):
            freq, val = heapq.heappop(heap)
            output.append(val)
        return output