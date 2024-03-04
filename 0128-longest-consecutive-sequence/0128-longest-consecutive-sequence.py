class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxlen = 0
        
        for num in nums:
            curr = 1
            
            if num-1 not in nums_set: # First element of the consec sequence
                while num+1 in nums_set: # If next value element in set too
                    curr+=1
                    num+=1
                    
                maxlen = max(maxlen, curr)
                
        return maxlen