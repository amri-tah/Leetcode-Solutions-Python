# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        length = 0
        while temp:
            length+=1
            temp=temp.next

        part = length//k
        remainder=length%k
        result = []
        current = head
        
        for i in range(k):
            if remainder>0:size=part+1
            else: size=part
            
            remainder -= 1
            if size==0: 
                result.append(None)
                continue
        
            part_head = current
            for j in range(size - 1):
                if current: current = current.next
            
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            result.append(part_head)
        
        return result
            

