class Solution:
    def rob(self, nums: List[int]) -> int:
        first,second=0,0
        
        for i in range(len(nums)):
            second,first=max(first+nums[i],second),second
           
        return second
                