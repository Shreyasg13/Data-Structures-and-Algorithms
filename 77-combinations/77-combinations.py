class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        self.dfs(range(1,n+1), k, 0, [], ans)
        return ans
    
    def dfs(self,nums,k,index,path,ans):
        if  k==0:
            print(path)
            ans.append(path)
            return
        for i in range (index,len(nums)):
            self.dfs(nums,k-1,i+1,path+[nums[i]],ans)
         
            
            
            
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
        
    
        
        