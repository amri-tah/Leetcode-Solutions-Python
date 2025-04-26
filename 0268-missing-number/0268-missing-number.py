class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set, i = set(nums), 0
        while i in nums_set:
            i+=1
        return i
        