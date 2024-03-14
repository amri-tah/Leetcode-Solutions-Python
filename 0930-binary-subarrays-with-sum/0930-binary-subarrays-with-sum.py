class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count, currsum = 0, 0
        freq = {}
        for num in nums:
            currsum+=num
            if currsum==goal: count+=1
            if currsum-goal in freq: count += freq[currsum - goal]
            freq[currsum] = freq.get(currsum, 0)+1
            
        return count
    
    
    