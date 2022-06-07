# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        
    
        def Depth(root):
            if not root:
                return 0
            l=Depth(root.left) 
            r=Depth(root.right)
            self.res=max(l+r,self.res)
            return 1+max(l,r)
        
        Depth(root)
        return self.res
        
        
    
    
    
    
#     class Solution(object):
#     def diameterOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         self.ans = 0
        
#         def depth(p):
#             if not p: return 0
#             left, right = depth(p.left), depth(p.right)
#             self.ans = max(self.ans, left+right)
#             return 1 + max(left, right)
            
#         depth(root)
#         return self.ans