class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-f, v) for v, f in freq.items()]
        heapq.heapify(heap)
        res = []
        while k:
            f, v = heapq.heappop(heap)
            res.append(v)
            k-=1
        return res