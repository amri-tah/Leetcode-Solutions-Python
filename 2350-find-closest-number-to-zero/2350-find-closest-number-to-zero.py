class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minDist, value = float('inf'), None
        for num in nums:
            if abs(num)<minDist or (abs(num)==minDist and num>value):
                minDist, value = abs(num), num
        return value