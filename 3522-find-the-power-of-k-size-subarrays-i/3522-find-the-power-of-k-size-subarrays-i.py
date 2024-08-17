class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n-k+1):
            consec = True
            for j in range(1, k):
                if nums[i+j]!=nums[i+j-1]+1: consec = False
            if consec: result.append(max(nums[i:i+k]))
            else: result.append(-1)
        return result