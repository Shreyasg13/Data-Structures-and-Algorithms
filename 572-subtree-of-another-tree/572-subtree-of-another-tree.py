# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Helping function to check if Subtree is same as current root tree
        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False            
            if p and q:
                return p.val==q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        # if it reaches end i.e. it could not found and same tree
        if not root:
                return False
        # if current root and subtree are same
        if isSameTree(root,subRoot) :
                return True
        # keep recursing function on left and right side of tree    
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)  
        
        