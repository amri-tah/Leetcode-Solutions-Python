class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        if len(nums)==2: return abs(nums[1]-nums[0])

        nums.sort()
        subarray = [0]*len(nums)
        for i in range(1, len(nums)):
            subarray[i] = nums[i]-nums[i-1]
        return max(subarray)