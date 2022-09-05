# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        level,q=[],deque()
        if root:
            q.append((root,0))
        else:
            return []
        Map=defaultdict(list)
        
        while q:
            level=[]
            for i in range(len(q)):
                
                node,x_axis=q.popleft()
                level.append([node.val,x_axis])
                
                if node.right:
                    q.append( (node.right , x_axis+1) )
                if node.left:
                    q.append( (node.left , x_axis-1) )
                
            for n,x in sorted(level):
                Map[x].append(n)    
            
            print(Map)
        res=[]
        
        for key in sorted(Map.keys()):
            res.append(Map[key])
      
        
        return res
       
            
            
            
        
        