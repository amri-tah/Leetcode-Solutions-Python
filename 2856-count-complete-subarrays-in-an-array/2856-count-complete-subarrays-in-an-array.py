class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k, count = len(set(nums)), 0
        for i in range(len(nums)):
            unique = set()
            for j in range(i, len(nums)):
                unique.add(nums[j])
                if len(unique) == k: count += 1
        return count