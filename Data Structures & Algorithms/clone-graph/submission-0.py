"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}

        def dfs(old):
            # Check if old node has a corresponding new node
            if old in hashmap:
                return hashmap[old]
            
            # If not then create a new node
            copy = Node(val = old.val)

            # Add copy to hashmap
            hashmap[old] = copy

            # Add neighbors
            for n in old.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node) if node else None