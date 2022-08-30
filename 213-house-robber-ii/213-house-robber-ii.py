class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(nums):
            f,s=0,0
            for i in range(len(nums)):
                s,f=max(nums[i]+f,s),s
            return s
        print(nums[0:-1])
        return max(rob_linear(nums[1:]),rob_linear(nums[0:-1]),nums[0])