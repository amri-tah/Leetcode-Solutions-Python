class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # output minVal: for [minVal nums] which needs all values to be >=1
        minVal = curr = 0
        for num in nums:
            curr+=num
            minVal = min(minVal, curr)
        return 1-minVal