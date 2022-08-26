# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        res=[]
        if root:
            stack.append(root)
        
        while stack:
            level=[]
            for i in range(len(stack)):
                # keep poping first node and append it to current level
                node=stack.pop(0)
                level.append(node.val)
                # keep storing left and right child in stack
                if node.right   :  stack.append(node.right)
                if node.left    :  stack.append(node.left)
            # after each level form keep appending that node in res
            res.append(level[0])
            
        return res
        
#         res, stack= [], [root] 
#         if not root:
#             return []
#         while stack:
#             res.append(stack[-1].val) # appending right most value
#             level, stack = stack, []
#             for node in level: # build the next level
#                 if node.left: stack.append(node.left)
#                 if node.right: stack.append(node.right)
                    
#         return res
                
