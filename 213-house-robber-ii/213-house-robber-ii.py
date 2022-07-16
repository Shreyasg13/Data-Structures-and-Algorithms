class Solution:
    def rob(self, nums: List[int]) -> int:
        # finding max among 1 to n-1 and n to 1  and first element
        return max( nums[0],self.rob_with_linear(nums[1:]) , self.rob_with_linear(nums[0:len(nums)-1]) )
        
    def rob_with_linear(self,amount):
        fir,sec=0,0
        for i in range(len(amount)):
            fir,sec=sec,max(fir+amount[i],sec)
        return sec