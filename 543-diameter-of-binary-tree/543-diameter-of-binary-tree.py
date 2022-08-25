# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        
        def DFS(root):
            if not root:return 0
            
            l,r=DFS(root.left),DFS(root.right)
            self.diameter=max(l+r,self.diameter)
            print(l,r,self.diameter)
            return 1+max(l,r)
        
        DFS(root)
        return self.diameter
        
