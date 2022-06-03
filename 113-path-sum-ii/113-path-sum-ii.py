# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        self.dfs(root,targetSum,[],res)
        return res
        
    
    
    def dfs(self,root,total,path,res):
       
       
        # print(path,total,sum(path),res)
        # path.append(root.val)
        # res.append(path)
        if not root:  
            return
        
        if total == sum(path)+ root.val and not root.left and not root.right :
            print("inn")
            path.append(root.val)
            res.append(path)
            return
           
        # if total < sum(path) + root.val and total > 0 :
        #     return
        # if total > sum(path) + root.val and total < 0 :
        #     return
           
        if root.left  :
            print("L")
            self.dfs(root.left,total,path+[root.val],res)
        if root.right :
            print("R")
            self.dfs(root.right,total,path+[root.val],res)
            
            
#             [-2,null,-3]
# -5
        
       
       