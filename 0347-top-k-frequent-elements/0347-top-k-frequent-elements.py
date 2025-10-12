class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        
        # heap = [(-f, v) for v, f in freq.items()]
        # heapq.heapify(heap)
        # while k:
        #     f, v = heapq.heappop(heap)
        #     res.append(v)
        #     k-=1
        # return res

        buckets = [[] for _ in range(len(nums)+1)]
        for val, count in freq.items():
            buckets[count].append(val)
        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res)==k: return res