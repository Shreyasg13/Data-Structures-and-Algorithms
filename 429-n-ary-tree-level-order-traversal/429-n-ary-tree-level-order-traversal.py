"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        q=deque()
        if root:
            q.append(root)
        else:
            return []
        while q:
            
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                
                if node.children:
                    for c in node.children:
                        q.append(c)
            
            res.append(level)
        return res
            
        
        