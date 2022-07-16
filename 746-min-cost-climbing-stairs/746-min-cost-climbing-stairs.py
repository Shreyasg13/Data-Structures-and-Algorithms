class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
         # revesing the array start at 10 
            # [10,15,20]
        for i in range(len(cost)-3,-1,-1):
            # checking fist step and second step min
            cost[i]+=min(cost[i+1],cost[i+2])  
        return min(cost[0],cost[1])
        
        