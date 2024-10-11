"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        clone = {None: None}
        curr = head
        while curr:
            newNode = Node(curr.val)
            clone[curr]=newNode
            curr = curr.next
        
        curr = head
        while curr:
            copy = clone[curr]
            copy.next = clone[curr.next]
            copy.random = clone[curr.random]
            curr = curr.next

        return clone[head]