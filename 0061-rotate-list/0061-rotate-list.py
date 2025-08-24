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
        k%=length
        if k==0: return head
        last = head
        for _ in range(length-k-1):
            last = last.next
        start, dummy = last.next, last
        while dummy.next:
            dummy=dummy.next
        last.next = None
        dummy.next = head
        return start

