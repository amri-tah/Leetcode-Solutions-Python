# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(next=head)
        prev = dummy
        
        # Move prev to the node before left position
        for _ in range(left - 1):
            prev = prev.next
        
        # curr first node in the sublist
        curr = prev.next
        
        for _ in range(right - left):
            node = curr.next
            curr.next = node.next
            node.next = prev.next
            prev.next = node
        
        return dummy.next