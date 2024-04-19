# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        temp = head
        length = 0
        while temp:
            length+=1
            temp = temp.next
        
        k %= length
        prev = curr = head
        
        for _ in range(k):
            curr = curr.next
        while curr.next:
            prev = prev.next
            curr = curr.next
        curr.next = head
        head = prev.next
        prev.next = None
        return head