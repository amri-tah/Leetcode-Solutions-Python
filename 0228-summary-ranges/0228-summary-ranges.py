class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        for num in nums:
            if output and output[-1][1]+1==num:
                output[-1][1] = num
        
            else:
                output.append([num, num])
        
        return [f"{start}->{end}" if start!=end else f"{start}" for start, end in output]
        