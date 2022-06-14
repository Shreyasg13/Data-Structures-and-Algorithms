class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        self.dfs(candidates,target,[],0,res)
        return res
    
    def dfs(self,candidates,target,path,index,res):
        
        if target < 0:
            return
        if target==0 and path not in res:
            res.append(path)
            
        for i in range(index,len(candidates)):
            if candidates[i]==candidates[i-1] and i > index:
                continue
            self.dfs(candidates,target-candidates[i],path+[candidates[i]],i+1,res)