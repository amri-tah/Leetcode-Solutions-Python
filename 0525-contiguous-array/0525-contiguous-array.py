class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxL = prefixSum = 0
        hash = {0: -1} # sum: earliest index
        # if 1 encountered => +1
        # if 0 encountered => -1
        # [-1, 0]
        # [-1, 0, -1]
        # [-1, 0, 1, 2, 3, 2, 1, 0]
        for i, num in enumerate(nums):
            prefixSum+=1 if num==1 else -1
            if prefixSum in hash: maxL = max(maxL, i-hash[prefixSum])
            else: hash[prefixSum]= i
        return maxL
