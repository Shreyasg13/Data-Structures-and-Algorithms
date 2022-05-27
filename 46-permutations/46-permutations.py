class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # visit=[False]*len(nums)  
        # ans=[]
        # element=[]
        
        def dfs(nums,ele=[],ans=[]):
            if not nums:
                
                ans.append(ele.copy())
               
            for i in range(len(nums)):
                rem=nums[:i]+nums[i+1:]
                ele.append(nums[i])
                dfs(rem,ele,ans)
                ele.pop()
            return ans
                    
        return dfs(nums)
        
         
            
            
            
            
            
#             def permute(self, nums):
# 	# helper
# 	def recursive(nums, perm=[], res=[]):
# 		if not nums: # -- NOTE [1] 
# 			res.append(perm[::]) #  -- NOTE [2] - append a copy of the perm at the leaf before we start popping/backtracking

# 		for i in range(len(nums)): # [1,2,3]
# 			newNums = nums[:i] + nums[i+1:]
# 			perm.append(nums[i])
# 			recursive(newNums, perm, res) # - recursive call will make sure I reach the leaf
# 			perm.pop() # -- NOTE [3] 
# 		return res

# return recursive(nums)