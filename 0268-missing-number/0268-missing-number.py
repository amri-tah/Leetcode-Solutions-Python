class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # approach 1: sort, then iterate
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i: return i
        # return len(nums)

        # approach 2: put into a set and check what is missing
        # num_set = set(nums)
        # for i in range(len(nums) + 1):
        #     if i not in num_set: return i

        # approach 3: sum
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
       

