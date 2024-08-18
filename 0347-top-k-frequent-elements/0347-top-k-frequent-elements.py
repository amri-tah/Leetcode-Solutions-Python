class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result, bucket = [], [[] for i in range(len(nums)+1)]

        for key, val in freq.items():
            bucket[val].append(key)
        for i in range(len(nums), 0, -1):
            for n in bucket[i]: 
                result.append(n)
                if len(result)==k: return result
