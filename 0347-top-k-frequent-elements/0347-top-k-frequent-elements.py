class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
        
        freq = [key for key, value in sorted(d.items(), key = lambda x: x[1], reverse=True)]
        return freq[0:k]


