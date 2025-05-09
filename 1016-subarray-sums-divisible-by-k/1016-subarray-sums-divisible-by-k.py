class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        count = curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            rem = curr%k
            count += prefixSum.get(rem, 0)
            prefixSum[rem]=prefixSum.get(rem, 0)+1
        return count