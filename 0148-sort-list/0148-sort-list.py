# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Merge sort
        # 1) Get the middle node, set the next ptr of middle to None
        # 2) Sort left and right halves
        # 3) Merge left and right halves
        
        # Base Case: when head is None or only 1 element
        if not head or not head.next:
            return head
        
        # Get middle node
        middle = self.getMiddle(head)
        # Set left, right halves
        left = head
        right = middle
        temp = right.next
        right.next = None
        right = temp
        
        # Sort Left and Right halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge and return the sorted lists
        return self.merge(left, right)
    
    def getMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def merge(self, left, right):
        dummy = ListNode()
        head = dummy
        while left and right:
            if left.val>right.val:
                head.next = right
                right = right.next
            else:
                head.next = left
                left = left.next
            head = head.next
        
        if left:
            head.next = left
        elif right:
            head.next = right
            
        return dummy.next