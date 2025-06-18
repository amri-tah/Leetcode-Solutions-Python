class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum, i = 0, sum(nums), 0
        while i<len(nums):
            rightSum-=nums[i]
            if leftSum == rightSum: return i
            leftSum+=nums[i]
            i+=1
        return -1