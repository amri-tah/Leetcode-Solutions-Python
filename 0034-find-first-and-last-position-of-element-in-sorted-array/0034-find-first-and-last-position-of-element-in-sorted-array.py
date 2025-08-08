class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, 0
        res = [-1, -1]
        while left<len(nums):
            if nums[left]==target:
                res[0]=left
                right = left
                while right<len(nums) and nums[right]==nums[left]:
                    right+=1
                res[1]=right-1
                break
            left+=1
        return res
        
