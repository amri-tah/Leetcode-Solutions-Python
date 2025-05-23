class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash = {0: 1}  # {sum: count}
        prefixSum = count = 0
        for num in nums:
            prefixSum += num
            if prefixSum - goal in hash:
                count += hash[prefixSum - goal]
            hash[prefixSum] = hash.get(prefixSum, 0) + 1
        return count
