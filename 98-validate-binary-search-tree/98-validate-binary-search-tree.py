# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
        def check(root,low,high):
            # if it reaches end of the node i.e. it is valid BST
            if not root:
                return True
            # if node is in  valid range keep checking for left and right child 
            if low < root.val < high:
                # node val < right < high
                # low < left < node val
                return check(root.right,root.val,high) and check(root.left,low,root.val)
            else :
                # early rejection for invalid node
                return False
        return check(root,float('-inf'),float('inf'))
                