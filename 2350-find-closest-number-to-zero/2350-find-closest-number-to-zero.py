class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minDist = nums[0]
        for num in nums:
            if abs(num)<=abs(minDist): minDist = num

        if minDist<0 and abs(minDist) in nums: return abs(minDist)
        else: return minDist