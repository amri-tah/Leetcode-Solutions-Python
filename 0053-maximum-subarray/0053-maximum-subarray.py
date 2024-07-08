class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -1e8
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            maxSum = max(maxSum, curr)
            if (curr < 0): curr=0
        return maxSum