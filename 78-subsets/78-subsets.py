class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans=[]
#         subset=[]
        
#         def dfs(i):
#             if i >= len(nums):
#                 ans.append(subset.copy())
#                 return
            
            
#             subset.append(nums[i])
#             dfs(i+1)
#             subset.pop()
#             dfs(i+1)
        
#         dfs(0)
#         return ans
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.dfs(nums,[],0,res)
        return res
    
    def dfs(self,nums,path,index,res):
        res.append(path)
        for i in range (index,len(nums)):
            self.dfs(nums,path+[nums[i]],i+1,res)
            
        