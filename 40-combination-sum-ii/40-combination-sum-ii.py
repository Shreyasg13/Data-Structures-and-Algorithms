class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        self.dfs(candidates,target,0,[],ans)
        return ans
    
    def dfs(self,nums,target,index,path,ans):
        if target < 0:
            return
        if target==0:
            ans.append(path)
            return
           
        
        for i in range (index,len(nums)):
            if nums[i]==nums[i-1] and i>index:
                continue
            self.dfs(nums,target-nums[i],i+1,path+[nums[i]],ans)
            
            
            
            
            
#             def combinationSum2(self, candidates, target):
#     res = []
#     candidates.sort()
#     self.dfs(candidates, target, 0, [], res)
#     return res
    
# def dfs(self, candidates, target, index, path, res):
#     if target < 0:
#         return  # backtracking
#     if target == 0:
#         res.append(path)
#         return  # backtracking 
#     for i in xrange(index, len(candidates)):
#         if i > index and candidates[i] == candidates[i-1]:
#             continue
#         self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res)
            
        

        