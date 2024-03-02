class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # approach 1: simply square each and then sort
        # approach 2: sort irrespective of sign 
        # approach 3: 2 ptrs 
        
        left, right, i = 0, len(nums)-1, len(nums)-1
        output = [0]*len(nums)
        while left<=right:
            if nums[left]**2>=nums[right]**2:
                output[i]=nums[left]**2
                left+=1
            else:
                output[i]=nums[right]**2
                right-=1
            i-=1
        return output