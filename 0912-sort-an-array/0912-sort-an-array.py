class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minnums = -min(nums)
        nums = [a+minnums for a in nums]

        for i in range(len(str(max(nums)))):
            count = [0]*10
            out = [0]*len(nums)

            for j in nums:
                ind = int((j/10**i)%10)
                count[ind] += 1
            
            for k in range(1, len(count)):
                count[k] += count[k-1]

            for l in range(len(nums)-1,-1,-1):
                ind = int((nums[l]/(10**i)%10))
                count[ind] -= 1
                out[count[ind]] = nums[l]
            nums = out
        
        nums = [a-minnums for a in nums]
        return nums