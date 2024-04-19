class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(curr):
            if len(curr)==len(nums):
                result.append(curr)
                return
            
            for num in nums:
                if num not in curr: backtrack(curr+[num])
        
        backtrack([])
        return result