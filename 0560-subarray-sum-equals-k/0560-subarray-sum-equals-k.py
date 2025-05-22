class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum  = {0: 1} # {sum: no of times the sum has occured}
        curr = count = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr-k in prefixSum: count+=prefixSum[curr-k]
            prefixSum[curr] = prefixSum.get(curr, 0)+1
        return count