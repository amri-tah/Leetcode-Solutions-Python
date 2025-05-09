class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum  = {0: 1}
        curr = count = 0
        for i in range(len(nums)):
            curr += nums[i]
            count += prefixSum.get(curr-k, 0)
            prefixSum[curr] = prefixSum.get(curr, 0)+1
        return count