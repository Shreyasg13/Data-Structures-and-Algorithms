"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # create a map of node
        Map={}
        
        def DFS(node):
            # if node found in map then return a node
            if node in Map:
                return Map[node]
            # create a deep copy and push it in a map 
            copy=Node(node.val)
            Map[node]=copy
            # also append the neighbours of current node recursively
            for nei in node.neighbors:
                copy.neighbors.append(DFS(nei))
            
            return copy
            
        return DFS(node) if node else None
