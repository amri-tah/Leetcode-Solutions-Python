class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j, n = 0, len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[j] = nums[i]
                j+=1
        while j<n:
            nums[j]=0
            j+=1