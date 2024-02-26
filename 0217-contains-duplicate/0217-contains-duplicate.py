class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        for right in range(1, len(nums)):
            if nums[left]!=nums[right]:
                left = right
            else:
                if right-left+1>=2: return True
        return False