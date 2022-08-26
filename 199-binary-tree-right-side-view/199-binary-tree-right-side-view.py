# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        if root:
            stack.append(root)
        while stack:
            level=[]
            for i in range(len(stack)):
                node=stack.pop(0)
                level.append(node.val)
                
                if node.right   :  stack.append(node.right)
                if node.left    :  stack.append(node.left)
            
            res.append(level[0])
            
        return res
