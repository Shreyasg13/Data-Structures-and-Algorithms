class Solution:
    def climbStairs(self, n: int) -> int:
        # top down approach
        last,prev=1,1
        
        while n-1 > 0:
            last,prev=prev,prev+last
            n-=1
        
        return prev
