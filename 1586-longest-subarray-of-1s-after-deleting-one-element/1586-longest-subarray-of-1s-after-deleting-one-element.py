class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxwidth, zeroes, left = 0, 0, 0
        for right in range(len(nums)):
            if nums[right]==0: zeroes+=1
            if zeroes<=1: maxwidth = max(maxwidth, right-left)
            else: 
                while zeroes>1:
                    if nums[left]==0: zeroes-=1
                    left+=1
        return maxwidth