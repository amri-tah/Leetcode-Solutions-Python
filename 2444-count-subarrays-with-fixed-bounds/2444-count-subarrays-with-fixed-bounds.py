class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        # out of range element index, minK val index, maxK val index
        notinrange = left = right = -1

        for i in range(len(nums)) :
            if not minK <= nums[i] <= maxK: notinrange = i
            if nums[i] == minK: left = i
            if nums[i] == maxK: right = i
            result += max(0, min(left, right) - notinrange)
        return result