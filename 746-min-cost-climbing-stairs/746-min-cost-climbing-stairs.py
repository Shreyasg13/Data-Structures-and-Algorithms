class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10,15,20] 0
        
        # top down apprach
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
            
        return min(cost[0],cost[1])
        
        