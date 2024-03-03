# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length of LL
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        
        dummy = ListNode(0, head)
        prev = dummy
        
        # Bring prev to length-n-1
        for _ in range(length-n):
            prev = prev.next

        # Delete node
        prev.next = prev.next.next
        
        return dummy.next