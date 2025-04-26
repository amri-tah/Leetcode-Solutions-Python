class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes, n = 0, len(nums)
        for i in range(n):
            if nums[i] and (i==0 or not nums[i-1]):
                curr = 1
                while i<n-1 and nums[i+1]:
                    curr+=1
                    i+=1
                maxOnes = max(maxOnes, curr)
        return maxOnes