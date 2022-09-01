# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        """
        with Deque of Q((node,max_val))
            1.poping node and max_value
            2.keep on checking if its good node or node
            3.push nodes in q if left or right child exist with updated max values  
            
        """
        
        q=collections.deque()
        q.append((root,float('-inf'))) #q((root,max_value))
        res=0
        
        while q:

            root,max_val=q.popleft() 
            
            if max_val <=root.val:
                res+=1
            
            if root.left:
                q.append((root.left,max(root.val,max_val)))
            if root.right:
                q.append((root.right,max(root.val,max_val)))
        
        return res