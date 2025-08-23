class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def backtrack(i):
            if i>=len(nums)-1: return 0
            if i in cache: return cache[i]
            minjump = float('inf')
            for j in range(1, nums[i]+1):
                if i+j<len(nums): minjump=min(minjump, 1+backtrack(i+j))
            cache[i]=minjump
            return minjump
        return backtrack(0)