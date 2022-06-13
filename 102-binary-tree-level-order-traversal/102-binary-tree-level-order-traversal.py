# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque()
        if root:q.append(root)
        
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res
            
            
       
            
#     def levelOrder(self, root):
        
#         if not root:
#             return []
#         ans, level = [], [root]
#         while level:
#             print(ans)
#             ans.append([node.val for node in level])
#             temp = []
#             for node in level:
#                 temp.extend([node.left, node.right])
#             level = [leaf for leaf in temp if leaf]
#         return ans