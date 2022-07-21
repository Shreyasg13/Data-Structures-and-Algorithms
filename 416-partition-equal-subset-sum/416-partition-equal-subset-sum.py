class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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
       
        
        return True if target in dp else False
