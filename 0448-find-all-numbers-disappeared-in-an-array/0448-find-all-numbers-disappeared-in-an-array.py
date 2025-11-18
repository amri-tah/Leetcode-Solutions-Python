class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numset = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in numset: res.append(i)
        return res
