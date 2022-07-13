# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        return self.check(root.left,root.right)
    
    def check(self,l,r):
            
            if  l and r:
                return l.val==r.val and self.check(l.left,r.right) and self.check(l.right,r.left)
            return l==r
                