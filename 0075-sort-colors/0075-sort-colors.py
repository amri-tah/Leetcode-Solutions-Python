class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        for i in range(len(nums)):
            if i<freq[0]: nums[i]=0
            elif i>=freq[0] and i<freq[0]+freq[1]: nums[i]=1
            else: nums[i]=2
                