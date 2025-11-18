class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {i: 0 for i in range(1, len(nums)+1)}
        for num in nums:
            freq[num]+=1
        res = [-1, -1]
        for k, v in freq.items():
            if v==2: res[0]=k
            if v==0: res[1]=k
        return res