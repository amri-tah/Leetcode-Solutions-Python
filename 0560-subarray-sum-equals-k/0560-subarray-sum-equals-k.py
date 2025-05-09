class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        curr = count = 0
        for i in range(len(nums)):
            curr += nums[i]
            count += prefixSum[curr-k]
            prefixSum[curr] += 1
        return count