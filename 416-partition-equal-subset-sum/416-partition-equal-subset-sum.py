class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # target=sum(nums)//2
        # return False if sum(nums)%2==0 else self.dfs(nums,target,0)
        target=sum(nums)//2
        if sum(nums)%2==1:
            return False
       
        dp=set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            new_dp=set()
            for ele in dp:
                new_dp.add(ele)
                new_dp.add(ele+nums[i])
            dp=new_dp
       
        if target in dp:
            return True
        else:
            return False
                
#     def dfs(self,candidates,target,index):
        
#         if target < 0:
#             return
#         elif target==0:
#             return True
#         for i in range(index,len(candidates)):
#             self.dfs(candidates,target-candidates[i],i+1)       
#         return False
