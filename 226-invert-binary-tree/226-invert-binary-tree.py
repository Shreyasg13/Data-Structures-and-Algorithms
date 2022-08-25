# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root return None
        if not root:
            return None
        # if both root exist keep on swapping
        if root.left or root.right:
            root.right,root.left=root.left,root.right
        # keep doing same for their left and right child
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root