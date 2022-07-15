# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, stack= [], [root] 
        if not root:
            return []
        while stack:
            res.append(stack[-1].val) # appending right most value
            level, stack = stack, []
            for node in level: # build the next level
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return res
                
            
#          ## RC ##
#         ## APPROACH : BFS ##
        
# 		## TIME COMPLEXITY : O(N) ##
# 		## SPACE COMPLEXITY : O(D)##    (diameter)

#         if(not root): return []
#         queue = deque([root])
#         res = []
#         while (queue): 
#             curr_level = []
#             size = len(queue)
#             for i in range(size):
#                 curr = queue.popleft()
#                 if i == size - 1:
#                     res.append(curr.val)
#                 if (curr.left): 
#                     queue.append(curr.left)
#                 if (curr.right): 
#                     queue.append(curr.right)
#         return res         
            
         
                
   