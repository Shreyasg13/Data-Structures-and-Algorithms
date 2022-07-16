class Solution:
    def rob(self, nums: List[int]) -> int:
        return max( nums[0],self.rob_with_linear(nums[1:]) , self.rob_with_linear(nums[:-1]) )
        
    def rob_with_linear(self,amount):
        fir,sec=0,0
        for i in range(len(amount)):
            fir,sec=sec,max(fir+amount[i],sec)
        return sec