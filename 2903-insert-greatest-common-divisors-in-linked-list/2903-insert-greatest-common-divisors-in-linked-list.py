# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a%b)

        prev = head
        curr = prev.next
        while curr:
            newNode = ListNode(val=gcd(prev.val, curr.val), next=curr)
            prev.next = newNode
            prev = curr
            curr = curr.next
        return head