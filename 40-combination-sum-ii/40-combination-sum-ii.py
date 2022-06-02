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
            
            
            
            
            

            
        

        