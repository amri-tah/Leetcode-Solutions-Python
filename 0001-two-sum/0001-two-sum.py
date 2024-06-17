class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}
        for i in range(len(nums)):
            rem = target-nums[i]
            if rem in remaining:
                return [i, remaining[rem]]
            else:
                remaining[nums[i]] = i
                