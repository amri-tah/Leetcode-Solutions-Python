class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxval =  max(nums)
        left, right = 0, 0
        maxlen = 0
        while right<len(nums):
            if nums[right]==maxval:
                while right<len(nums) and nums[right]==nums[left]:
                    right+=1
                maxlen=max(maxlen, right-left)
            right+=1
            left=right
        return maxlen