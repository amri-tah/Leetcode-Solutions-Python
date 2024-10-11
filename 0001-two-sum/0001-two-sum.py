class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i, num in enumerate(nums):
            rem = target-num
            if rem in val: return [val[rem], i]
            else: val[num]=i