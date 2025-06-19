class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxwidth, zeroes, left = 0, 0, 0
        for right in range(len(nums)):
            if nums[right]==0: zeroes+=1
            if zeroes<=k: maxwidth = max(maxwidth, right-left+1)
            else: 
                while zeroes>k:
                    if nums[left]==0: zeroes-=1
                    left+=1
        return maxwidth