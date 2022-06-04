# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	# all possible paths from node n
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node, total):
            if not node:
                return 0 
            return (node.val == total) + dfs(node.left, total-node.val) + dfs(node.right, total-node.val)
        
        if not root:
            return 0
        
		# returns possible paths from each node
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)            
        
        