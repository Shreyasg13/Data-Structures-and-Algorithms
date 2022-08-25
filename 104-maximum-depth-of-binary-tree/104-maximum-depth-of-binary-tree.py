# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        # keep going to left and right end 
        l=1+self.maxDepth(root.left)
        r=1+self.maxDepth(root.right)
        return max(l,r)
            
        
        
        
        