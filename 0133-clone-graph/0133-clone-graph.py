"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        # hash map to map every original node to its duplicate
        hashmap = {}

        # perform dfs on the original and create new vertices and edges
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            newNode = Node(val=node.val, neighbors=[])
            hashmap[node] = newNode
            for neigh in node.neighbors:
                newNode.neighbors.append(dfs(neigh))
            return newNode

        return dfs(node)

