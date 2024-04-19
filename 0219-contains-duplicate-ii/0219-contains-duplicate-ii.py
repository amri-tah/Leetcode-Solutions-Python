class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups= {}
        for i, num in enumerate(nums):
            if num in dups and i-dups[num]<=k: return True
            dups[num] = i
        return False