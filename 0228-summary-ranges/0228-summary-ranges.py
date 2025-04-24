class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        for num in nums:
            if output and output[-1][-1]+1==num: output[-1][-1] = num
            else: output.append([num, num])
        for i in range(len(output)):
            first, second = output[i][0], output[i][1]
            if first!=second: output[i]=f"{first}->{second}"
            else: output[i]=f"{first}"
        return output