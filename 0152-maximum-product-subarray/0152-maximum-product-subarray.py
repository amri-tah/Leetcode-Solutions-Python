class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        result = max(nums)

        for n in nums:
            if n==0: currMax, currMin = 1, 1
            else:
                temp = currMax*n
                currMax = max(currMax*n, currMin*n, n)
                currMin = min(temp, currMin*n, n)
                result = max(result, currMax)
        return result