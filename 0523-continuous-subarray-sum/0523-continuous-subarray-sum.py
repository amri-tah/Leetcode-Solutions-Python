class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixRem = {0: -1}
        currSum = 0

        for i, num in enumerate(nums):
            currSum += num
            rem = currSum % k
            if rem in prefixRem:
                if i - prefixRem[rem] >= 2: return True
            else: prefixRem[rem] = i
        return False

        