class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, temp = 0, 0
        for num in nums:
            if num==0: 
                temp+=1
                res+=temp
            else: temp=0
        return res