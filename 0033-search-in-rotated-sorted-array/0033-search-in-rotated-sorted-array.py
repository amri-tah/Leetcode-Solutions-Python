class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2

            # if mid in target
            if nums[mid]==target: return mid

            # if left side sorted
            if nums[mid]>=nums[left]:
                if target>nums[mid] or target<nums[left]: left=mid+1
                else: right=mid-1
            
            # if right side sorted
            else:
                if target<nums[mid] or target>nums[right]: right=mid-1
                else: left=mid+1
        
        return -1