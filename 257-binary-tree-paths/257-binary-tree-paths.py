# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        self.dfs(root,"",ans)
        return ans
    
    
    def dfs(self,root,path,res):
        
       
        if root.left:
            self.dfs(root.left,path+str(root.val)+"->",res)
        if root.right:
            self.dfs(root.right,path+str(root.val)+"->",res)
        
        if not root.left and not root.right:
            res.append(path+str(root.val))
            return
                

            
#              # dfs recursively
#     def binaryTreePaths(self, root):
#         if not root:
#             return []
#         res = []
#         self.dfs(root, "", res)
#         return res
    
#     def dfs(self, root, ls, res):
#         if not root.left and not root.right:
#             res.append(ls+str(root.val))
#         if root.left:
#             self.dfs(root.left, ls+str(root.val)+"->", res)
#         if root.right:
#             self.dfs(root.right, ls+str(root.val)+"->", res)
            
            
            
            
        
#     def dfs(self,root,path,res):
#         path.append(root)
    
#         if not root:
#             return
#         if not root.left or not root.right:
#             path+="->"
#             self.dfs(root.left,path)
            
            
            
            