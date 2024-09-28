class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            nums[i] = sum(int(digit) for digit in str(num))
        return min(nums)