class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        # Starting Backwards
        for i in range(len(nums),-1,-1):
            # Finding max consecutive seq len in [i ..len(nums)]
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        
        return max(dp)