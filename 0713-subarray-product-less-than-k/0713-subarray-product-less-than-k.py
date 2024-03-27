class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        # Using a sliding window
        count, mult, left = 0, 1, 0
        for right in range(len(nums)):
            mult *= nums[right] 
            while mult >= k:
                mult //= nums[left]  
                left += 1
            count += right - left + 1  

        return count