class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for pivot in range(len(nums)):
            rightSum = total - leftSum - nums[pivot]
            if rightSum==leftSum: return pivot
            leftSum+=nums[pivot]
        
        return -1