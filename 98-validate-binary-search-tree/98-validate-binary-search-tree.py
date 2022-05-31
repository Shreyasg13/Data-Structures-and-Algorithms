# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            def isValidBST(self, root, INT_MAX = float('inf'), INT_MIN = float('-inf')):
                
                if not root:
                    return True
                if root.val <= INT_MIN or root.val >= INT_MAX:
                    return False
                print(root.val,INT_MAX,INT_MIN)
                return self.isValidBST(root.left, min(INT_MAX, root.val), INT_MIN) and self.isValidBST(root.right, INT_MAX, max(root.val, INT_MIN))
        

  