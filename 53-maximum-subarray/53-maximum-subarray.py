class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum=nums[0]
        cur_sum=0
        
        for ele in nums:
        # recomputing sum from zero when negetive sum occurs    
            if cur_sum < 0:
                cur_sum=0
            
            cur_sum+=ele
        # computing current max
            max_sum=max(max_sum,cur_sum)
            
        return max_sum