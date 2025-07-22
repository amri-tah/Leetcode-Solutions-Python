class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix, left, maxscore = 0, 0, 0
        unique = set()
        for right, num in enumerate(nums):
            while num in unique:
                unique.remove(nums[left])
                prefix -= nums[left]
                left += 1
            unique.add(num)
            prefix += num
            maxscore = max(maxscore, prefix)

        return maxscore