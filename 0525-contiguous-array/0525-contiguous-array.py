class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash = {0: -1}
        maxlen, count = 0, 0
        for i in range(len(nums)):
            
            count += 1 if (nums[i] == 1) else -1
            if count in hash:
                maxlen = max(maxlen, i-hash[count])
            else:
                hash[count]=i
        return maxlen;
