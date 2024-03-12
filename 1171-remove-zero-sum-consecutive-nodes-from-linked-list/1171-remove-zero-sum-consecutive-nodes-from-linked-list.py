# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = head
        
        sum = 0
        sums = {0: dummy}

        while current:
            sum += current.val
            if sum in sums:
                prev = sums[sum].next
                temp = sum + prev.val
                while prev != current:
                    del sums[temp]
                    prev = prev.next
                    temp += prev.val
                sums[sum].next = current.next
            else:
                sums[sum] = current
            current = current.next

        return dummy.next