# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack=[]
        if root:
            stack.append(root)
        else:
            return []
        avg=[]
        while stack:
            level,stack=stack,[]
            s=0
            for n in level:
                s+=n.val
            avg.append(s/len(level))
            
            for node in level:
                if node.left:
                    stack.append(node.left)
               
                if node.right:
                    stack.append(node.right)
               
        return avg
            