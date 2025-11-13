class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = [0]*len(nums)
        n1, n2 = 0, len(nums)//2
        for i in range(len(nums)):
            if i%2==0: 
                out[i]=nums[n1]
                n1+=1
            else:
                out[i]=nums[n2]
                n2+=1
        return out