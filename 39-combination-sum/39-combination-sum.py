class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        # candidates.sort()
        self.dfs(candidates,target,0,[],res)
        return res
    def dfs(self,nums,target,index,path,res):
        if target < 0:
            return
        if target==0:
            res.append(path)
            return
        for i in range(index,len(nums)):
            self.dfs(nums,target-nums[i],i,path+[nums[i]],res)
        
        
        
        
                    
#     def combine(self, n, k):
#         res = []
#         self.dfs(range(1,n+1), k, 0, [], res)
#         return res
    
#     def dfs(self, nums, k, index, path, res):
#         #if k < 0:  #backtracking
#             #return 
#         if k == 0:
#             res.append(path)
#             return # backtracking 
#         for i in range(index, len(nums)):
#             self.dfs(nums, k-1, i+1, path+[nums[i]], res)
        
    
        