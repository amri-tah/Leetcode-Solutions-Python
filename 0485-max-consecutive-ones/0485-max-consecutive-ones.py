class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        l, r = 0, 0
        while r<len(nums):
            if nums[l]==1:
                while r < len(nums) and nums[r]==1:
                    r+=1
                maxones = max(maxones, r-l)
                l=r
            else:
                l+=1
                r=max(l,r)
        return maxones