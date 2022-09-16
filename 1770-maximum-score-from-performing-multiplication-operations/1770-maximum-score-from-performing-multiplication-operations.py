class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def dfs(l,r,i):
            # Base Case
            if i==len(multipliers): 
                return 0
            # find the max from left side and right side and keep on 
            # calling function on left and right side 
            return max (nums[l]*multipliers[i] + dfs(l+1,r,i+1) ,
                        nums[r]*multipliers[i] + dfs(l,r-1,i+1))
        
        return dfs(0,len(nums)-1,0)
        
        
