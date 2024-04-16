# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast, slow = head, dummy
        while fast and fast.next:
            fast = fast.next.next
            
            # Slow pointer gets to the node right before the middle node
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next
        
        