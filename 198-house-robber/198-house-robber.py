class Solution:
    def rob(self, nums: List[int]) -> int:
        first,second=0,0
        # [first,second,n,n+1,.............]
        for i in range(len(nums)):
            temp=max(first+nums[i],second)
            first=second
            second=temp
            
        return second
        
       
    