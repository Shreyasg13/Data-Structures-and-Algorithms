class Solution:
    def climbStairs(self, n: int) -> int:
        # top down approach
        last,prev=1,1
        
        for i in range(n-1):
            # change the last to previous and simply keep updating previou \
            last,prev=prev,prev+last
        return prev
        