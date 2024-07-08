class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i>=0: # If not in descending order:
            for j in range(len(nums)-1, i, -1):
                if nums[j]>nums[i]: 
                    nums[j], nums[i] = nums[i], nums[j]
                    break

        nums[i+1:] = reversed(nums[i+1:])
        return nums