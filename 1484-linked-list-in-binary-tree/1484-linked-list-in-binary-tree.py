# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(bin_node, ll_node):
            if not ll_node: return True # reached end of LL
            if not bin_node: return False
            if bin_node.val == ll_node.val:
                return dfs(bin_node.left, ll_node.next) or dfs(bin_node.right, ll_node.next)
            return False

        if not root: return False
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)