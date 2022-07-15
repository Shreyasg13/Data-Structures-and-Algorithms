# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if reaches bottom of tree
        if not p and not q:
            return True
        # if one of the node is empty
        elif not p or not q:
            return False
            # check and calls tree recursively
        else:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            
            
            
            
        
       