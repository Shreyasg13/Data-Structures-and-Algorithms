# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(root,left,right):
            
            if not root:
                return True
            if left < root.val < right:
                return check(root.right,root.val,right) and check(root.left,left,root.val)
            else :
                return False
        return check(root,float('-inf'),float('inf'))
        