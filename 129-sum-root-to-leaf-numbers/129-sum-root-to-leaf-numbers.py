# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0)
    
    def dfs(self,root,pathsum):
                
        if not root :
            return 0
        else:
            pathsum=root.val + pathsum*10
        
        if not root.left and not root.right :
            return pathsum
            
        return self.dfs(root.left,pathsum) + self.dfs(root.right,pathsum)
            
       
            
       
            
            
            
        
        
        
            
            
    
    
        