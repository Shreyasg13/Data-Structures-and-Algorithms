class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        self.backtrack(nums,[],res)
        return res
    
    def backtrack(self,nums,path,res):
        
        if not nums:
            res.append(path)
        
        for i in range (len(nums)):
            
            self.backtrack(nums[:i]+nums[i+1:],path+[nums[i]],res)
            

        
      
    
    
    
    
    
    
    
    
    
        # visit=[False]*len(nums)  
        # ans=[]
        # element=[]
        
#         def dfs(nums,ele=[],ans=[]):
#             if not nums:
#                 print("check")
#                 ans.append(ele[::])
               
#             for i in range(len(nums)):          
#                 ele.append(nums[i])
#                 dfs(nums[:i]+nums[i+1:],ele,ans)
#                 print(ans)
#                 print("pop")
#                 ele.pop()
#             return ans
                    
#         return dfs(nums)

        
         
            
            
            
            
            
