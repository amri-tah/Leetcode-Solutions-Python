class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=0
        freq = [key for key, value in sorted(d.items(), key = lambda x: x[1], reverse=True)]
        return freq[0:k]


