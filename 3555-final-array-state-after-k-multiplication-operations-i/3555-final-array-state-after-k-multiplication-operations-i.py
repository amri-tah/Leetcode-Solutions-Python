class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if not nums: return nums
        for i in range(k):
            min_num = min(nums)
            min_index = nums.index(min_num)
            nums[min_index]=min_num*multiplier
        return nums