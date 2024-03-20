# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first, last = ListNode(next=list1), list1
        
        # Bring first and last pointers to its position
        for i in range(a):
            first = first.next
            last = last.next
            
        for i in range(b-a):
            last = last.next
        
        # Change the next value of the first pointer to the first node of list 2
        first.next = list2
        
        # Traverse till the end node of list2 
        while (list2.next is not None):
            list2 = list2.next
        
        # Point the last node of list2 to the last node of list1
        list2.next = last.next
        last.next = None
        
        return list1