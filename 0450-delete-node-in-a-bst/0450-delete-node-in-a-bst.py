# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return
        if root.val>key: root.left = self.deleteNode(root.left, key)
        elif root.val<key: root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: Node has no children
            if not root.left and not root.right: return None
            # Case 2: Node has only one child
            elif not root.left: return root.right
            elif not root.right: return root.left
            # Case 3: Node has two children
            else:
                # Find the inorder successor (minimum in right subtree)
                min_larger_node = self.helper(root.right)
                root.val = min_larger_node.val
                # Delete the inorder successor
                root.right = self.deleteNode(root.right, min_larger_node.val)
        return root
    
    def helper(self, head):
            while(head.left):
                head = head.left
            return head

        