class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums)==1: return 0
        # Set 2 pointers
        left, right = 0, len(nums)-1
        
        while left<=right:
            # Calculate mid index value
            mid = (left+right)//2
            # If value at mid is equal to target, FOUND
            if nums[mid]==target: return mid
            # If value at mid is less than target, 
            # the value might be found in the other half 
            elif nums[mid]<target: left = mid+1
            # If value is greater, the value might be in the left half of the array
            else: right = mid-1
        # If not found:
        return -1