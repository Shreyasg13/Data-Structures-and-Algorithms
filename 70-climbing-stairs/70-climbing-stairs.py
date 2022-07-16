class Solution:
    def climbStairs(self, n: int) -> int:
        last,prev=1,1
        for i in range(n-1):
            last,prev=prev,prev+last
        return prev
        