class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixSum =  count = 0
        hash = {0: 1} # prefsum: count 
        for num in nums:
            if num%2!=0: prefixSum+=1
            if prefixSum-k in hash: count+=hash[prefixSum-k]
            hash[prefixSum]=hash.get(prefixSum, 0)+1
        return count
