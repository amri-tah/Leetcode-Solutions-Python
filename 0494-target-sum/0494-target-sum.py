class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # brute force:

        # self.res = 0
        # def dfs(start, pathsum):
        #     if start==len(nums):
        #         if pathsum==target: self.res+=1
        #         return
        #     # 2 choices: + or -
        #     dfs(start+1, pathsum+nums[start])
        #     dfs(start+1, pathsum-nums[start])
        # dfs(0, 0)
        # return self.res

        # dp
        cache = {}
        def dfs(i, pathsum):
            if i==len(nums):
                if pathsum==target: return 1
                else: return 0
            if (i, pathsum) in cache: return cache[(i, pathsum)]
            cache[(i, pathsum)]=dfs(i+1, pathsum+nums[i])
            cache[(i, pathsum)]+=dfs(i+1, pathsum-nums[i])
            return cache[(i, pathsum)]
        return dfs(0, 0)
