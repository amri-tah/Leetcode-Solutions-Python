# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle
        fast, middle = head, head
        while fast and fast.next:
            fast=fast.next.next
            middle=middle.next
        
        # Reverse 2nd half
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        # Move pointers from front and back
        front = head
        maxsum = 0
        while prev:
            maxsum = max(maxsum, prev.val+front.val)
            front=front.next
            prev=prev.next
        return maxsum