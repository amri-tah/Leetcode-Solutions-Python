class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednums = sorted(nums)
        mapping = {}
        for i, v in enumerate(sortednums):
            if v not in mapping: mapping[v] = i 
        return [mapping[v] for v in nums]
