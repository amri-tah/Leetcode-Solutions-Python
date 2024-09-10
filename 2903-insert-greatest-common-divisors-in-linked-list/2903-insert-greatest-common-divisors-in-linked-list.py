# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            result = min(a, b)
            while result:
                if a % result == 0 and b % result == 0: break
                result -= 1
            return result
        
        prev = head
        curr = prev.next

        while curr:
            newNode = ListNode(val=gcd(prev.val, curr.val), next=curr)
            prev.next = newNode
            prev = curr
            curr = curr.next
        return head