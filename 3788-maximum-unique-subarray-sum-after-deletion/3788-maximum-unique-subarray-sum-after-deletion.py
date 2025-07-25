class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pos = set([num for num in nums if num>0])
        return max(nums) if len(pos)==0 else sum(pos)