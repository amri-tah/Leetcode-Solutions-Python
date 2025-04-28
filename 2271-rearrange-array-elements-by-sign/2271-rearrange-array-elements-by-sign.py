class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0]*n
        pos, neg = 0, 1
        for num in nums:
            if num>0:
                output[pos]=num
                pos+=2
            else:
                output[neg]=num
                neg+=2
        return output