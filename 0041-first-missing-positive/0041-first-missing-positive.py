class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = [False]*(len(nums)+1)
        for num in nums:
            if 0<num<=len(nums): visited[num]=True
        for num in range(1, len(nums)+1):
            if not visited[num]: return num
        return len(nums)+1
        