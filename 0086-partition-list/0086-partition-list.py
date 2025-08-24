# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        great = ListNode(0)
        greater = great
        less = ListNode(0)
        lesser = less
        curr = head
        while curr:
            if curr.val>=x:
                greater.next = curr
                greater=greater.next
            else:
                lesser.next=curr
                lesser=lesser.next
            curr=curr.next
        greater.next = None
        lesser.next = great.next
        return less.next