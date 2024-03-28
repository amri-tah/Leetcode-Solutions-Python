class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count, i = 0, -1
        freq = {}
        for j in range(len(nums)):
            freq[nums[j]]=freq.get(nums[j], 0)+1
            while freq[nums[j]]>k:
                i+=1
                freq[nums[i]]-=1
            count = max(count, j-i)
        return count