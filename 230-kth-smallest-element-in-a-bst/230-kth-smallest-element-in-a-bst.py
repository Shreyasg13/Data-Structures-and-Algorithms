# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k) -> int:
        nums=self.inorder(root)
        print(nums)
        return nums[k-1]
    
    def inorder(self,root):
        if not root:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)
    
        
    
        
#         stack=[]
#         n=0
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root=root.left
                
#             root=stack.pop()
#             n+=1
#             if n==k:
#                 return root.val
#             root=root.right
       
 
            
        