class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxval=max(nums)
        minval=min(nums)
        return (maxval-minval)*k