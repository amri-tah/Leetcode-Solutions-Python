class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = curr = left = 0
        maxElement = max(nums) # O(n)
        for right in range(len(nums)):
            if nums[right]==maxElement: curr+=1
            while curr >= k:
                if nums[left] == maxElement: curr -= 1
                left += 1
            count += left
        return count
            