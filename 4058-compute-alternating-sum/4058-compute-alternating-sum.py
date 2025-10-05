class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums), 2):
            res+=nums[i]
        for i in range(1, len(nums),2):
            res-=nums[i]
        return res