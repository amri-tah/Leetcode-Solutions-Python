# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # If no more elements to be made into a tree then None
        if not nums:
            return None
        
        # Get max value and its index in the list
        maximum = max(nums)
        index = nums.index(maximum)
        
        # Return the root node using recursion
        return TreeNode(val = maximum, 
                        left = self.constructMaximumBinaryTree(nums[:index]), 
                        right = self.constructMaximumBinaryTree(nums[index+1:]))
        