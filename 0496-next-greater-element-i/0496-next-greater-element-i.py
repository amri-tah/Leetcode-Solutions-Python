class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, output = [], [-1]*len(nums1)
        ind = {num:i for i, num in enumerate(nums1)}
        for num in nums2:
            while stack and num>stack[-1]:
                idx = ind[stack.pop()]
                output[idx]=num
            if num in ind: stack.append(num)
        return output