class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        for num in nums:
            if num-1 not in nums_set:
                current = num
                length = 1
                while current + 1 in nums_set:
                    current += 1
                    length += 1
                max_len = max(max_len, length)
        return max_len