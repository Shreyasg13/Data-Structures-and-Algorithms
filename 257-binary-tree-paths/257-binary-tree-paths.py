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
        
        # if left or right exist : recursing along with adding path
        if root.left:
            self.dfs(root.left,path+str(root.val)+"->",res)
        if root.right:
            self.dfs(root.right,path+str(root.val)+"->",res)
       # if end node end it and append the path 
        if not root.left and not root.right:
            res.append(path+str(root.val))
            return
                
