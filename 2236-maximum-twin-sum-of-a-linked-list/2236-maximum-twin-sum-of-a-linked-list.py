# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxtwinsum = 0
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        while prev:
            maxtwinsum = max(maxtwinsum, head.val+prev.val)
            head = head.next
            prev = prev.next
        return maxtwinsum