class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Mem={} #(index,target) Memorry array
        
        def dfs(i,t):
            # Base Case
            if i==len(nums):
                return 1 if t==target else 0
            # if result found in Mem
            if (i,t) in Mem:
                return Mem[(i,t)]
           
            # keep on storing data at index i in Memory
            Mem[(i,t)]=dfs(i+1,t-nums[i]) + dfs(i+1,t+nums[i]) 
            return Mem[(i,t)]
        
        return dfs(0,0)
       