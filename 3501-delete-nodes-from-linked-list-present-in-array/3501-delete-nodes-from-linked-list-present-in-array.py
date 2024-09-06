# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, curr = dummy, head
        nums = set(nums)
        # move curr while curr.val in nums
        while curr:
            if curr.val in nums: prev.next = curr.next
            else: prev = curr
            curr = curr.next
        return dummy.next