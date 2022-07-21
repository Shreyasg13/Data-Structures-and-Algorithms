class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)//2
        if sum(nums)%2==1:
            return False
       
        dp=set()
        dp.add(0)
        # keep on adding the possible combinations of sum 
        for i in range(len(nums)-1,-1,-1):
            new_dp=set()
            for ele in dp:
                # also adding current element for not loosing the pre 
                if ele==target or ele+nums[i]==target:
                    return True
                new_dp.add(ele)
                new_dp.add(ele+nums[i])
            dp=new_dp
       
        
        return True if target in dp else False
    
    
                    
#     def dfs(self,candidates,target,index):
        
#         if target < 0:
#             return
#         elif target==0:
#             return True
#         for i in range(index,len(candidates)):
#             self.dfs(candidates,target-candidates[i],i+1)       
#         return False

