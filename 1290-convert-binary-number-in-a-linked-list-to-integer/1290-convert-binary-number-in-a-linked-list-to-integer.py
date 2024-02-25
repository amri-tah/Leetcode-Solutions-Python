# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        n = 0
        while current:
            n+=1
            current = current.next
        print(n)
        # n = 3
        current = head
        output = 0
        while current:
            n-=1
            output+= (2**n)*current.val
            current = current.next
        return output
            