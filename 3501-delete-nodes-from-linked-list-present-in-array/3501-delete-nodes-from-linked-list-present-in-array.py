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
            while curr and curr.val in nums:
                curr = curr.next
            prev.next = curr
            prev = curr
            if curr: curr = curr.next
        return dummy.next