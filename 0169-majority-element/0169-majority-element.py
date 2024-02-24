class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        max = 0
        for num in nums:
            if num in freq: freq[num] += 1
            else: freq[num] = 1
        
        for num in freq:
            if freq[num]>max:
                max = freq[num]
                value = num
        return value